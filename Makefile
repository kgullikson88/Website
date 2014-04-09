all: gen

gen: 
	hyde gen

serve: clean gen
	hyde serve

clean:
	rm -rf deploy

gen-production: clean
	hyde gen -c production.yaml

publish: gen-production	
	rsync -e ssh -r deploy_production/ kgulliks@astro.as.utexas.edu:/home/astro/edu/kgulliks/www/
