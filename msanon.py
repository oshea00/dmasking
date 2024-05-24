from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer import AnalyzerEngine, RecognizerResult, EntityRecognizer

analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

results = analyzer.analyze(text="My phone number is 123-456-7890", entities=["PHONE_NUMBER"], language="en")
anonymized_text = anonymizer.anonymize(text="My phone number is 123-456-7890", analyzer_results=results)
print(anonymized_text)  # 'My phone number is <PHONE_NUMBER>'

