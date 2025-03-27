import os

folder = './datasets/OfficeHome/'
domains = os.listdir(folder)
domains.sort()

for d in range(len(domains)):
	dom = domains[d]
	if os.path.isdir(os.path.join(folder, dom)):
		dom_new = dom.replace(" ","_")
		print(dom, dom_new)
		os.rename(os.path.join(folder, dom), os.path.join(folder, dom_new))

		classes = os.listdir(os.path.join(folder, dom_new))
		classes.sort()
		# print(classes)
		f = open(dom_new[0] + "_list.txt", "w")
		for c in range(len(classes)):
			cla = classes[c]
			cla_new = cla.replace(" ","_")
			print(cla, cla_new)
			os.rename(os.path.join(folder, dom_new, cla), os.path.join(folder, dom_new, cla_new))
			files = os.listdir(os.path.join(folder, dom_new, cla_new))
			files.sort()
			# print(files)
			for file in files:
				file_new = file.replace(" ","_")
				os.rename(os.path.join(folder, dom_new, cla_new, file), os.path.join(folder, dom_new, cla_new, file_new))
				print(file, file_new)
				full_path = os.path.join(folder, dom_new, cla_new, file_new)
				full_path = os.path.normpath(full_path).replace('\\', '/')
				print(f'{full_path} {c}')
				f.write(f'{full_path} {c}\n')

		f.close()
