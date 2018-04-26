from Crypto.Hash import SHA256
from collections import defaultdict

msga="Melbourne Cup: $8,000 on Horse 'Phar Lap' (Secret Number) [transaction id: {}]"
msgb="Melbourne Cup: $8,000 on Horse 'Sunline' (Excess Knowledge) [transaction id: {}]"
total_hashes = 0
m_dict = defaultdict(int)
while True:
	filled_msga = msga.encode("ascii")
	filled_msgb = msgb.encode("ascii")
	h1 = SHA256.new(filled_msga).hexdigest()[:8]
	h2 = SHA256.new(filled_msgb).hexdigest()[:8]
	m_dict[h2] = total_hashes
	if h1 in m_dict.keys():
		print(total_hashes)
		print(m_dict[h1])
		break
	total_hashes+=1
