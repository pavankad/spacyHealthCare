from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import pandas as pd
import pdb

class icd10_dictionary():
    def __init__(self, icd10_file=None):
        self.dictionary, self.all_conditions = self.read_icd10_file(icd10_file)

        self.confidenceLevels = pd.DataFrame({
            'wordLength': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            #'minRatio': [100, 100, 100, 100, 80, 80, 80, 80, 75, 75]
            'minRatio': [100, 100, 100, 100, 100, 100, 70, 70, 60, 60]
        })

    def getFuzzyRatio(self, token=None, confidence_levels_enabled=True, default_level=85):
        """
        This function is meant to retrieve the matching minimum similarity ratio for a particular string length.
        As string length decreases, you should work with higher ratios to ensure you are not matching words that shouldn't match.
        """

        # Check for appropriate formats
        assert isinstance(token, str), "Tokens can be str() type only"

        # We check if confidence levels are set
        if confidence_levels_enabled:
            for i, row in self.confidenceLevels.iterrows():
                if len(token) > self.confidenceLevels['wordLength'].max():
                    min_ratio = self.confidenceLevels['minRatio'].min()
                else:
                    min_ratio = \
                    self.confidenceLevels.loc[self.confidenceLevels['wordLength'] == len(token)]['minRatio'].values[0]

        # Fallback if confidence levels are not set
        else:
            min_ratio = default_level

        return int(min_ratio)

    def getFuzzySimilarity(self, token=None, min_ratio=None):
        """
        This function uses the FuzzyWuzzy library to find the highest matching similary score of a token in a list of values.
        We then compare the similary score of the fuzzy match with our minimum threshold and return a match if the match > treshold.
        """

        # Check for appropriate formats
        assert isinstance(token, str), "Tokens can be str() type only"
        assert isinstance(self.dictionary, dict), "Dictionary format should be provided in the dictionary parameter."
        assert isinstance(min_ratio, int), "Integer format should be provided in the minimum-ratio parameter."

        # for key, values in dictionary.items():
        # Using the process option of FuzzyWuzzy, we can search through the entire dictionary for the best match
        match = process.extractOne(token, self.all_conditions, scorer=fuzz.ratio)
        # Match is a tuple with the match value and the similary score.
        if min_ratio <= match[1]:
            key = self.dictionary[match[0]]
        else:
            key = 'NO_KEY'
            match = (token, 0)
        return (match + (key,))

    def read_icd10_file(self, filepath):
        # Read ICD codes 2023 files and create a dictionary/map (condition -> Code mapping)
        df = pd.read_csv(filepath)
        pdb.set_trace()
        df.set_index('Condition', inplace=True)
        dictionary = df.to_dict()['Code']
        all_conditions = df.index.tolist()
        return dictionary, all_conditions

    def lkup(self, entities):
        icd_codes = []
        for ent in entities:
            token = ent['text']
            fuzzy_ratio = self.getFuzzyRatio(token=token, confidence_levels_enabled = True)
            icd_code = self.getFuzzySimilarity(token=token, min_ratio=fuzzy_ratio)
            icd_codes.append(icd_code)
        return icd_codes

