class Solution:
	def distinctEchoSubstrings(self, text: str) -> int:
		res = []
		for i in range(len(text)):
			for j in range(i+1,len(text)+1):
				if len(text[i:j])%2==0 and text[i:j][:len(text[i:j])//2]==text[i:j][len(text[i:j])//2:] and text[i:j] not in res:
					res.append(text[i:j])
		return len(res)