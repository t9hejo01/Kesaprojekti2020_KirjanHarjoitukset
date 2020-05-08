kieli = ['englanti', 'ruotsi', 'saksa', 'ranska', 'venaja', 'espanja']

print("Alkuperainen lista")
print(kieli)

print("Lista aakkosjarjestyksessa")
print(sorted(kieli))

print("Alkuperainen lista jalleen")
print(kieli)

print("Lista aakkosjarjestyksessa takaperin")
print(sorted(kieli, reverse=True))

print("lista takaperin")
kieli.reverse()
print(kieli)

print("Alkuperainen lista jalleen")
kieli.reverse()
print(kieli)

print("Lista aakkosjarjestyksessa")
kieli.sort()
print(kieli)
