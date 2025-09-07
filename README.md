# **WIT Wyższa Szkoła Informatyki Stosowanej i Zarządzania**

# 

# APO Algorytmy przetwarzania obrazów

Prowadzący \- **Anna Korzyńska**  
Autor \-  **Igor Rasiński**

Napisana przeze mnie aplikacja składa się z głównego menu, poniżej, wszystkie wbudowane funkcje są umieszczone w zakładach Lab. Natomiast operacje otwierania, zamykania, zapisywania plików są w zakładce File.
![obraz](https://github.com/IgorRas/APO/blob/master/images/image27.png)

Spis treści

1. Wprowadzenie  
   1. Wymagania  
   2. Uruchomienie programu  
2. Lab1  
   1. Histogram  
      1. Monochromatic  
      2. Color  
3. Lab2  
   1. Stretch Histogram  
      1. Linear  
      2. Nonlinear  
   2. Equalize  
   3. Negative  
   4. Thresholding 1 param  
   5. Thresholding 2 param  
4. Lab3  
   1. Add  
   2. Add Number  
   3. Multiply  
   4. Divide  
   5. Subtract  
   6. Logic operations   
      1. NOT  
      2. AND  
      3. OR  
      4. XOR  
5. Lab4  
   1. Smoothing  
   2. Sharpen  
   3. Detecting edges  
   4. Median  
6. Lab5  
   1. Edges with operators  
   2. Thresholding interactive  
7. Lab6  
   1. Erosion  
   2. Dilation  
   3. Open\_morf  
   4. Close\_morf  
   5. Moment  
8. File  
   1. Open  
   2. Save  
   3. Duplicate

# 1.Wprowadzenie

## 1.1 Wymagania Wymagane oprogramowanie:
\- system operacyjny Windows 7 lub wyższy
\- Python 3.7 lub wyższy 
#### Następujące biblioteki dla języka Python:
\- Pillow 9.2.0
\- PySimpleGui 4.60.4
\- OpenCV-Python 4.6.0.66
\- Matplotlib 3.5.3
\- Numpy 1.21.6

## 1.2 Uruchamianie programu

By uruchomić program korzystamy z konsoli. Znajdując się w lokalizacji, w której   
znajduje się projekt, należy wpisać “python main.py”.

# 2.Lab1

## 2.1 Histogram

2.1.1 Monochromatic  
Wylicza i wyświetla okno histogramu dla obrazu szaroodcieniowego wraz z samym obrazem.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image40.png) 
2.1.2 Color  
Wylicza i wyświetla okno histogramu dla obrazu kolorowego wraz z samym obrazem. Wyświetlają się trzy histogramy, oddzielne dla każdego koloru.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image41.png)

# 3.Lab2

## 3.1 Stretch histogram

3.1.1 Linear  
Po kliknięciu w opcję pokazuje się okno wyboru progu maksymalnego i minimalnego. Po wybraniu pokazuje się obraz i jego zmodyfikowany histogram.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image42.png)

![obraz](https://github.com/IgorRas/APO/blob/master/images/image18.png)  
3.1.1 Nonlinear  
Po kliknięciu w opcję pokazuje się okno wyboru gammy. Potem pokazuj sie zmodyfikowany histogram.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image46.png) 
3.2 Equalize   
Wyświetla obraz oraz histogram zmodyfikowanego obrazu. Zmiana polega na rozciągnięciu histogramu obrazu do maksymalnych wartości.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image33.png) 
3.3 Negative  
Wyświetla obraz oraz histogram zmodyfikowanego obrazu. Zmiana polega odwróceniu stworzeniu negatywu podanego obrazu.
![obraz](https://github.com/IgorRas/APO/blob/master/images/image43.png)
3.4 Thresholding 1 param  
Po uruchomieniu pojawia się okno wyboru progu.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image26.png) 
Potem wyświetla odpowiednio zmodyfikowany obraz i histogram.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image34.png)
3.5 Thresholding 2 param  
Po uruchomieniu pojawia się okno wyboru dwóch progów.

![obraz](https://github.com/IgorRas/APO/blob/master/images/image44.png)
Potem wyświetla odpowiednio zmodyfikowany obraz i histogram.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image17.png)

# 4.Lab3

4.1 Add  
Po uruchomieniu pojawia się okno wyboru obrazu. Ten obraz zostanie dodany do pierwotnego obrazu. Następnie wyświetlony zostanie ten obraz.  
4.2 Add number  
Po uruchomieniu pojawia się okno wyboru liczby. Liczba ta zostanie dodana do całego histogramu pierwotnego obrazu. Następnie wyświetlony zostanie ten obraz.  
4.3 Multiply  
Po uruchomieniu pojawia się okno wyboru liczby. Histogram pierwotnego obrazu zostanie pomnożony przez nią. Następnie wyświetlony zostanie ten obraz i jego histogram.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image15.png)
4.4 Divide  
Po uruchomieniu pojawia się okno wyboru liczby. Histogram pierwotnego obrazu zostanie podzielony przez nią. Następnie wyświetlony zostanie ten obraz.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image47.png)  
4.5 Subtract  
Po uruchomieniu pojawia się okno wyboru obrazu. Następnie od pierwotnego obrazu zostanie odjęty wybrany i wyświetlony wynik.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image8.png)![obraz](https://github.com/IgorRas/APO/blob/master/images/image5.png)![obraz](https://github.com/IgorRas/APO/blob/master/images/image13.png)
4.6 Logic operators  
Każda z opcji wykonuje logiczne operacje bitowe na zadanych obrazach.  
4.6.1 NOT  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image12.png)
4.6.2 AND  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image5.png)
![obraz](https://github.com/IgorRas/APO/blob/master/images/image7.png)
![obraz](https://github.com/IgorRas/APO/blob/master/images/image28.png)
4.6.3 OR  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image5.png)
![obraz](https://github.com/IgorRas/APO/blob/master/images/image7.png)
![obraz](https://github.com/IgorRas/APO/blob/master/images/image19.png)
4.6.4 XOR  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image5.png)
![obraz](https://github.com/IgorRas/APO/blob/master/images/image7.png)
![obraz](https://github.com/IgorRas/APO/blob/master/images/image6.png)

# 5.Lab4

5.1 Smoothing  
Po uruchomieniu wyświetla się okno wyboru opcji. Następnie wykonuje wybraną operację i wyświetla obraz oryginalny i po zmianie.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image14.png) 
![obraz](https://github.com/IgorRas/APO/blob/master/images/image9.png)  
5.2 Sharpen  
Po uruchomieniu wyświetla się okno wyboru opcji. Następnie wykonuje wybraną operację i wyświetla obraz oryginalny i po zmianie.

![obraz](https://github.com/IgorRas/APO/blob/master/images/image45.png)  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image10.png) 
5.3 Detecting edges   
Po uruchomieniu wyświetla się okno wyboru opcji. Następnie wyświetla obraz oryginalny oraz zadane krawędzie.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image29.png) 
![obraz](https://github.com/IgorRas/APO/blob/master/images/image30.png)
5.4 Median   
Po uruchomieniu wyświetla się okno wyboru opcji. Następnie wykonuje wybraną operację i wyświetla obraz oryginalny i po zmianie.

![obraz](https://github.com/IgorRas/APO/blob/master/images/image38.png)  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image39.png)

# 6.Lab5

6.1 Edges with operators  
Przeprowadza operację wykrycia krawędzi z danym operatorem. Po uruchomieniu wyświetla się okno wyboru opcji. Następnie wyświetlają się wykryte krawędzie.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image24.png)
![obraz](https://github.com/IgorRas/APO/blob/master/images/image23.png)
6.2 Thresholding interactive  
Przeprowadza operację progowania, zgodnie z zadanymi opcjami i wyświetla porównanie oryginału z obrazem modyfikowanym.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image37.png)
Wynik progowania adaptacyjnego, metodą gaussowską  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image36.png)

# 7.Lab6

7.1 Erosion  
Przeprowadza binaryzację oryginalnego obrazu i następnie jego erozję. Wyświetla obydwa obrazy.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image31.png) 
7.2 Dilation  
Przeprowadza binaryzację oryginalnego obrazu i następnie jego dyfuzję. Wyświetla obydwa obrazy.

![obraz](https://github.com/IgorRas/APO/blob/master/images/image32.png)
![obraz](https://github.com/IgorRas/APO/blob/master/images/image11.png)
7.3 Open\_morf  
Przeprowadza binaryzację oryginalnego obrazu i otwarcia wykorzystując podstawowy element strukturalny dysk 3x3.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image21.png) 
7.4 Close\_morf  
Przeprowadza binaryzację oryginalnego obrazu i zamknięcia wykorzystując podstawowy element strukturalny dysk 3x3.  
![obraz](https://github.com/IgorRas/APO/blob/master/images/image20.png)
7.5 Moment  
Wykonuje algorytm wyznaczający następujące cechy obiektu binarnego:  
\-momenty  
\-pole powierzchni i obwód  
\-współczynniki kształtu: aspectRatio (![obraz](https://github.com/IgorRas/APO/blob/master/images/image1.png)),  
extent (![obraz](https://github.com/IgorRas/APO/blob/master/images/image2.png)),   
solidity (![obraz](https://github.com/IgorRas/APO/blob/master/images/image3.png)),  
equivalentDiameter (![obraz](https://github.com/IgorRas/APO/blob/master/images/image4.png)).  
A następnie zapisuje je do pliku typu excel.

# 8.File

8.1 Open  
Otwiera eksplorator windows w celu wybrania obrazu. Będzie on później obrazem oryginalnym dla wykonywanych operacji.  
8.2 Save  
Zapisuje wybrany obraz w wybranej lokalizacji  
8.3 Duplicate  
Tworzy kopię wybranego obrazu. Zostanie ona usunięta po zakończeniu działania programu.
