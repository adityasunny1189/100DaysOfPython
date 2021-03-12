# Cofee Machine

resources = {
	"water": 300,
	"cofee": 100,
	"milk": 300
}

cofee_types = {
	"latte": {
			"water": 100,
			"cofee": 24,
			"milk": 150
	},
	"cappachino": {
			"water": 150,
			"cofee": 24,
			"milk": 100
	},
	"normal": {
			"water": 50,
			"cofee": 18,
			"milk": 0
	}
}

print(cofee_types['latte']['water'])

