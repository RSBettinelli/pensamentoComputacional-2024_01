# i am using the OS import to see how many collumns
# is yout terminal using
from shutil import get_terminal_size	# the default line size will be based on the terminal collumns.


TIPO_UN = 'un'
TIPO_KG = 'kg'


def window_size():			# get the opened terminal size
	size = get_terminal_size()
	width = int(size[0])
	height = int(size[1])
	return [width, height]
	
	
def size_table_price():			# will set the table divider
	size = get_terminal_size()
	width = int(size[0])

	first = round((width - 10) / 2)		# first element size (name)
	second = int((width - 10) / 8)		# second element size (price)
	third = int((width - 10) / 8)		# third element size (amount)
	fourth = round((width - 10) / 4)	# fourth element size (subtotal)

	while int(first) + int(second) + int(third) + int(fourth) + 10 != width:	#without this line, sometimes the the size will be wrong
		third += 1
		
	return([int(first), int(second), int(third), int(fourth)])


def is_valid_number(number: str) -> list | None:
	itens_list = obter_catalogo_de_produtos()
	
	for item in itens_list:			
		if number == item["codigo"]:	# if the input is in the list codes
			return item
	return None


def obter_catalogo_de_produtos() -> list:
	return[
		{
			'nome': 'Batata branca',
			'tipo': TIPO_KG,
			'preco': 8.99,
			'codigo': '100',
		},
		{
			'nome': 'Cebola roxa',
			'tipo': TIPO_KG,
			'preco': 7.55,
			'codigo': '110',
		},
		{
			'nome': 'Cenoura',
			'tipo': TIPO_KG,
			'preco': 6.99,
			'codigo': '120',
		},
		{
			'nome': 'Margarina sem sal 500g',
			'tipo': TIPO_UN,
			'preco': 8.55,
			'codigo': '200',
		},
		{
			'nome': 'Leite desnatado 1L',
			'tipo': TIPO_UN,
			'preco': 4.99,
			'codigo': '210',
		},
		{
			'nome': 'Sabão em pó 4kg',
			'tipo': TIPO_UN,
			'preco': 25.99,
			'codigo': '220',
		},
		{
			'nome': 'Chaleira inox 2.7L',
			'tipo': TIPO_UN,
			'preco': 129,
			'codigo': '300',
		}
	]
