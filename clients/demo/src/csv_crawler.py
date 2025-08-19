import csv
from pathlib import Path
from typing import Optional
from crawler.files.main import FilesCrawler, run as run_file_crawler
from crawler.struct import ParsedDocument

class CSVCrawler(FilesCrawler):
    def handle_custom(self, file: Path) -> list[ParsedDocument]:
        if file.suffix != '.csv':
            return []
        results = []
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"Processing ticket: {row['title']}")
                results.append(ParsedDocument(
                    title=row['title'],
                    text=row['content'],
                    url=row['url'],
                    breadcrumbs=[row['project']],
                    metadata={"ticket_id": row['id']},
                ))
        return results

def run(conf):
    run_file_crawler(conf, crawler_class=CSVCrawler)