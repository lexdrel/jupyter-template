import pandas as pd
import random
import secrets

random.seed(42)

n = 200000

sources = ['other', 'email', 'context', 'undef']

rows = []
for _ in range(n):
    user_id = secrets.token_hex(4).upper()      # 8 hex chars
    source = random.choice(sources)
    email = secrets.token_hex(10) if random.randrange(7) < 4 else ""
    purchase = random.choice([0, 1])
    rows.append((user_id, source, email, purchase))


df = pd.DataFrame(rows, columns=['user_id','source','email','purchase'])
df.to_csv('visit_log.csv', index=False)