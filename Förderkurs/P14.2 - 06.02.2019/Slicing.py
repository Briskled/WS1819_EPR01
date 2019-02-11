s = "Lachsschaumspeise"
# gesucht: eipmacscL

print(s[::-2])



s1 = "acbbnnnjeftdesnaT"
# gesucht: Tnetennba
print(s1[::-1][::2])


s2 = "99811233377"
# gesucht: 1337
print(s2[4]+s2[7:10])
print(s2[4::2])


s3 = "Die Antwort auf alles ist 42"
# gesucht: eautwA
print(s3[1::][::3][1:7][::-1])
print(s3[19:3:-3])
