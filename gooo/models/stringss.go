package main

import (
	"fmt"
	"strings"


)


func main(){
	baso := "halo"
	salinan := strings.Clone(baso)
	fmt.Println(salinan)

	compare := strings.Compare("hallo","allo")

	fmt.Println(compare)

	isi_contains := "hallo world"
	conten := strings.Contains(isi_contains,"oaso")
	fmt.Println("hasil dari", conten)

	bas := "hallo bass"
	content_any := strings.ContainsAny(bas,"hall" )
	fmt.Println(content_any)

	vountt := "beeeesep"
	hasil := strings.Count(vountt,"e")
	fmt.Println("hasilnya :",hasil)
	
	
	stringss := "the quickmy broder-in syster in baso lah"
	before,after,hasilnya := strings.Cut(stringss,"_")
	fmt.Println(before)
	fmt.Println(after)
	fmt.Println(hasilnya)

	str := "hallo world"
	ut := "hallo"
	hasi,_:= strings.CutPrefix(str,ut)
	fmt.Println("hasil nya", hasi)

	cuttt := "l"
	_,has:= strings.CutSuffix(str,cuttt)
	fmt.Println(has)

	banding := "hallo baso"
	banding_1 := "hallo BASO"
	hasil_1 := strings.EqualFold(banding,banding_1)
	fmt.Println("hasill dari  EqualFold",hasil_1)
}