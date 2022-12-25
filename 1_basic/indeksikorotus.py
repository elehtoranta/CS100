"""
COMP.CS.100: Indeksikorotus
Tekijä: Erkka Lehtoranta
Opiskelijanumero: ***REMOVED***

The program adds an index fix of 1.17 percent to the Finnish student aid amount.
"""

benefit_amount: float = float(input("Enter the amount of the study benefits: "))
index_raise: float = 0.0117  # 1.17 percent in decimal
print(f'If the index raise is {index_raise * 100} percent, '
      f'the study benefit,\n'
      f'after a raise, would be {benefit_amount * (index_raise + 1):.2f} euros')
benefit_amount *= (index_raise + 1)  # Update benefit to index adjusted amount
print(f'and if there was another index raise, the study\n'
      f'benefits would be as much as '
      f'{benefit_amount * (index_raise + 1):.2f} euros')
