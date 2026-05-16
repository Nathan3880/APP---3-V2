def policy_1(candidats, capacite):
    triés = sorted(candidats, key=lambda c: (-c['score'], c['timestamp'], c['id']))
    return triés[:capacite]

def policy_2(candidats, capacite):
    triés = sorted(candidats, key=lambda c: (
        -(c['score'] // 10) * 10,  
        -c['boursier'],             
        c['timestamp'],
        c['id']
    ))
    return triés[:capacite]


print("POLICY 1:", [c['id'] for c in policy_1(candidats, 2)])
print("POLICY 2:", [c['id'] for c in policy_2(candidats, 2)])
