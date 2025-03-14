from math import *
import streamlit as st

st.title("Kombinatorikk")
st.divider()
st.write("Denne webappen er basert på dei fire tellemåtane i kombinatorikk")

#st.logo("https://www.oisteing.com/images/logowww.png", link="https://www.oisteing.com")

st.logo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXL74BGleH6oFgRBkKovXDFNTb0h5U46mhnQ&s", link="https://www.github.com")


def ordna_uten(n,r):
    return(int(factorial(n)/factorial(n-r)))

def ordna_med(n,r):
    return(int(n**r))

def uordna_uten(n,r):
    return(int(factorial(n)/(factorial(n-r)*factorial(r))))


def uordna_med(n,k):
    return(int(factorial(n+k-1)/(factorial(n-1)*factorial(k))))



valg = st.selectbox(
    "Velg modell her",
    ("Ordna utvalg uten tilbakelegging", "Ordna utvalg med tilbakelegging", "Uordna utvalg uten tilbakelegging", "Uordna utvalg med tilbakelegging"),
)
st.divider()


#valg = int(st.number_input("Hva vil du gjøre? (1 - 4): ", value=1, max_value=4, min_value=1))
a=b=1

if valg=="Ordna utvalg uten tilbakelegging":
    st.header("Ordna utvalg utan tilbakelegging")
    st.write("Her skal du gjere r valg på eit utfallsrom som har n moglege når du starter, men der du ikkje legg tilbake.  \nSkriv inn n og så r")
    a=int(st.number_input("n: ", value=1, min_value=b))
    b=int(st.number_input("r: ", value=a, min_value=1, max_value=a))
    st.write("Når du har ",a," objekter og velger ",b," utan å leggje tilbake har du totalt ",ordna_uten(a,b), "mulige utvalg.")

if valg=="Ordna utvalg med tilbakelegging":
    st.header("Ordna utvalg med tilbakelegging")
    st.write("Da skal du gjere r valg basert på et utfallsrom med n moglegheitar.\nEksempel er tippekupongen.  \nSkriv inn n og så r")
    a=int(st.number_input("n: ", value=1, min_value=1))
    b=int(st.number_input("r: ", value=1, min_value=1))
    st.write(" Det er totalt ",ordna_med(a,b), "mulige utvalg.")

if valg=="Uordna utvalg uten tilbakelegging":
    st.header("Uordna utvalg uten tilbakelegging")
    st.write("Da skal du gjere r valg ut frå n moglegheitar.  \n Eksempel er lottokupongen. Skriv inn n og så r")
    a=int(st.number_input("n: ", value=1, min_value=1))
    b=int(st.number_input("r: ", value=a, min_value=1, max_value=a))
    st.write(" Det er totalt ",uordna_uten(a,b), "mulige utvalg.")

if valg=="Uordna utvalg med tilbakelegging":
    st.header("Uordna utvalg med tilbakelegging")
    st.write("Her skal du velge ut r frå ei mengde på n, men du legg tilbake det du velgjer kvar gong.  \nSkriv inn n og så r")
    a=int(st.number_input("n: ", value=1, min_value=1))
    b=int(st.number_input("r: ", value=1, min_value=1))
    st.write(" Det er totalt ",uordna_med(a,b), "mulige utvalg.")
