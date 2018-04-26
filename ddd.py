from Crypto.Hash import SHA256
from collections import defaultdict
msga="Melbourne Cup: $8,000 on Horse 'Phar Lap' (Secret Number) [transaction id: {%s}]"
msgb="Melbourne Cup: $8,000 on Horse 'Sunline' (Excess Knowledge) [transaction id: {%s}]"
msgc = "Melbourne Cup: $5,000 on Horse A (Secret Number) [transaction id: {%s}]"
total_hashes = 0
msg_dict = defaultdict(int)
while True:
	filled_msga = (msga % total_hashes).encode("ascii")
	filled_msgb = (msgb % total_hashes).encode("ascii")
	h1 = SHA256.new(filled_msga).hexdigest()[:8]
	h2 = SHA256.new(filled_msgb).hexdigest()[:8]
	msg_dict[h2] = total_hashes
	if h1 in msg_dict.keys():
		print(total_hashes)
		print(msg_dict[h1])
		break
	total_hashes += 1
