self.df = pd.json_normalize(posts)
self.df['length'] = self.df['line_count'].apply(self.categorize_length)
# collect unique tags
all_tags = self.df['tags'].apply(lambda x: x).sum()
self.unique_tags = list(set(all_tags))