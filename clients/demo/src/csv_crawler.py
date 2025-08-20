import csv
from pathlib import Path

# has the fields described here https://docs.serenitygpt.com/configuration/global/#overview
# and update_or_create method
from crawler.struct import ParsedDocument


THIS_DIR = Path(__file__).parent
def run(conf):
    for file in THIS_DIR.glob('*.csv'):
        print(f"Processing file: {file}")
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"Processing ticket: {row['title']}")
                doc = ParsedDocument(
                    title=row['title'],
                    text=row['content'],
                    url=row['url'],
                    breadcrumbs=[row['project']],
                    metadata={"ticket_id": row['id'], "document_type": "TCK"},
                )
                doc.update_or_create(conf.source)