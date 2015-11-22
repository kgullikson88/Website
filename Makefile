all: gen

gen: 
	hyde gen
	cp Continuum_Talk.html deploy/
	cp DistributingCode.html deploy/
	sed -e 's/Images/media\/images/g' -e 's/Figures/media\/images/g' CommitteeMeeting2015.html > deploy/CommitteeMeeting2015.html

serve: clean gen
	hyde serve

clean:
	rm -rf deploy

gen-production: clean
	hyde gen -c production.yaml
	cp Continuum_Talk.html deploy_production/
	cp DistributingCode.html deploy_production/
	sed -e 's/Images/media\/images/g' -e 's/Figures/media\/images/g' CommitteeMeeting2015.html > deploy_production/CommitteeMeeting2015.html

publish: gen-production	
	rsync -e ssh -r deploy_production/ kgulliks@astro.as.utexas.edu:/home/astro/edu/kgulliks/www/
