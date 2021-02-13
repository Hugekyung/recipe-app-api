import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""
    """데이터베이스 사용가능 전까지 Django실행을 중지하는 커맨드"""

    def handle(self, *args, **options):
        self.stdout.write('waiting for database...')  # 화면에 보여줄 내용
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second.')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
