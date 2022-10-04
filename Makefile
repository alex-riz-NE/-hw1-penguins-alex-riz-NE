.PHONY: data


# Download the data
# mkdir -p fails quietly if directory already exists
# curl -L follows indirects
# curl -O preserves filename of source
data:
	mkdir -p data
	cd data; curl -LO "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
	

# Create the chart
app:
	python -B src/app.py
	
	
clean:
	rm data/penguins.csv