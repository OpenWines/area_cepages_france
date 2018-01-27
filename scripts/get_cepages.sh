limits=( 07 08 09 10 11 12 13 14 )

for i in "${limits[@]}"
do
   wget -O output_$i.pdf http://www.observatoire-viti-france.com/docs/cvi/cvi$i/tableaux/t_scep_fr.pdf
   pdftohtml -noframes -s -xml output_$i.pdf output_$i.xml
done

wget -O output_06.pdf http://www.observatoire-viti-france.com/docs/cvi/cvi06/t_scep_fr.pdf
pdftohtml -noframes -s -xml output_06.pdf output_06.xml

python pdf_cepages.py

echo "type_cepage;surface_ha;wine_surface_proportion;year" > header.txt

cat header.txt output_*.csv > ../data/agrimer_all.csv
sed -i "s/;/,/g" ../data/agrimer_all.csv
cat ../data/agrimer_all.csv | grep -v TOTAL > ../data/area_cepages_france_yearly.csv
rm ../data/agrimer_all.csv

rm output_* header.txt
