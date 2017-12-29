events = [{
            'hour': 1,
            'recipient_email': 'foo@example.com'
        }, {
            'hour': 1,
            'recipient_email': 'foo@example.com'
        }, {
            'hour': 2,
            'recipient_email': 'bar@example.com'
        }, {
            'hour': 2,
            'recipient_email': 'bar@example.com'
        }, {
            'hour': 3,
            'recipient_email': 'baz@example.com'
        }, {
            'hour': 4,
            'recipient_email': 'foo@bar.com'
        }]

from collections import defaultdict

hour_count = defaultdict(int)

for event in events:
    if len(event['recipient_email']) < 40:
        hour_count[event['hour']] += 1

if sum(hour_count.values()) <= 4:
    hour_count = None
else:
    total = sum(hour_count.values())
    print(total)
    for i in range(24):
        if i not in hour_count:
            hour_count[i] = 0
        else:
            hour_count[i] = hour_count[i] / total

print(hour_count)

