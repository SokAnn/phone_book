export:
mysqldump -uroot -p db_users > /my_dump/dump.sql
password: root

import:
mysql -uroot -p db_users < /my_dump/dump.sql
password: root