import json
import re
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.exceptions import OutputParserException


def extract_json_from_text(text):
    """
    Extracts the first valid JSON object from a text using regex.
    """
    try:
        json_str = re.search(r'\{.*\}', text, re.DOTALL).group()
        return json.loads(json_str)
    except Exception as e:
        raise OutputParserException("Failed to extract valid JSON") from e


def extract_metadata(post):
    template = '''
You are given a LinkedIn post. Extract metadata in JSON format. 
Rules:
1. Respond with ONLY valid JSON. No explanation, no preamble.
2. Return a JSON object with exactly three keys: "line_count", "language", and "tags".
3. Extract at most 2 tags. 
4. Language should be either "English" or "Hinglish".

Post:
{post}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"post": post})

    # Try parsing with regex-based JSON extraction
    return extract_json_from_text(response.content)


def get_unified_tags(posts_with_metadata):
    unique_tags = set()

    for post in posts_with_metadata:
        unique_tags.update(post['tags'])

    unique_tags_list = ', '.join(unique_tags)

    template = '''
You will receive a list of tags. Your job is to unify and normalize them.
1. Merge similar tags into common standard tags.
   - Example: "Jobseekers", "Job Hunting" → "Job Search"
   - Example: "Motivation", "Inspiration", "Drive" → "Motivation"
2. Follow Title Case for all tags.
3. Return only a valid JSON with mapping from original tag to unified tag. No explanation or preamble.

Here are the tags:
{tags}
    '''
    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={"tags": str(unique_tags_list)})

    return extract_json_from_text(response.content)


def process_posts(raw_file_path, processed_file_path="data/processed_posts.json"):
    enriched_posts = []

    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)

        for post in posts:
            metadata = extract_metadata(post['text'])
            post_with_metadata = post | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags.get(tag, tag) for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_posts, outfile, indent=4)


if __name__ == "__main__":
    process_posts("data/raw_posts.json")
