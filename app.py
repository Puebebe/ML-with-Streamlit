import streamlit as st
import pickle

filename = "model.sv"
model = pickle.load(open(filename,'rb'))

def main():
	st.set_page_config(page_title="Czy pacjent wyzdrowieje po tygodniu leczenia?", page_icon=":face_with_thermometer:")
	overview = st.container()
	sliders = st.container()
	prediction = st.container()
	st.image("image.png")

	with overview:
		st.title("Czy pacjent wyzdrowieje po tygodniu leczenia?")

	with sliders:
		age_slider = st.slider(label="Wiek", value=44, min_value=11, max_value=77)
		symptoms_slider = st.slider(label="Liczba objawów", min_value=1, max_value=5)
		comorbidities_slider = st.slider(label="Liczba chorób współistniejących", min_value=0, max_value=5)
		height_slider = st.slider(label="Wzrost", min_value=124, max_value=200, help="Wzrost nie ma istotnego znaczenia dla rozpoznania stanu pacjenta, więc docelowo nie jest brany pod uwagę")

	data = [[symptoms_slider, age_slider, comorbidities_slider]]
	recovery = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dana osoba wyzdrowieje po tygodniu?\n### {0}".format("Tak" if recovery[0] == 0 else "Nie")) #*
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][recovery][0] * 100))

if __name__ == "__main__":
    main()

# "###### Opracowanie na podstawie omówienia przez Wojciecha Oronowicza-Jaśkowiaka [aplikacji](https://github.com/adamsquire/exploring_streamlit_apps) pierwotnie opisanej na blogu [Adam's Ramblings](https://adamsramblings.xyz/blog/exploring-streamlit-for-machine-learning-apps/)"
# "###### Źródło danych - [przykładowy zbiór fikcyjnych pacjentów](https://drive.google.com/file/d/16DE3ARyp5L9xKtMHDbB16R5qrTda5G06/view?usp=sharing)"
# '###### należy pamiętać, że nie są to dane prawdziwych pacjentów (również nie mamy określonej choroby, jakiej dotyczą)'
# '###### *może wydawać się, że model nie działa poprawnie, gdyż intuicyjnie wynik "powinien być" odwrotny'
# '###### dlatego warto byłoby "odwrócić" wartości w kolumnie \'zdrowie\' (czyli tej, której wartość chcemy przewidywać), tak aby 1 oznaczało wyzdrowienie, a 0 jego brak'