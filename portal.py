import streamlit as st

st.set_page_config(
    page_title = "CSS Portal",
    page_icon="https://media.licdn.com/dms/image/C4E0BAQGedJ9VG6zxhA/company-logo_200_200/0/1631379578669/one_2_ten_the_real_time_experience_rating_logo?e=2147483647&v=beta&t=ONOlsHI8M1pWa6EvmiKmeL2paPrVjp-N7NwUMXKStU8",
    layout="centered",
    initial_sidebar_state='collapsed'
    )



# Streamlit Options

st.header("CEO Light CSS Template Changer")

st.write("")

st.markdown("---")

st.write("")

bg_img = st.text_input(label = "I. Enter the url of the image to be used as survey background :-", value = "https://xmple.com/wallpaper/gradient-linear-green-grey-1920x1080-c2-006400-696969-a-90-f-14.svg")

st.write("")

start_button_bg_colour = st.color_picker(label = "II. Choose the colour for start button background :-", value = "#013220")

st.write("")

choices_bg_colour = st.color_picker(label = "III. Choose the colour for choices background :-", value = "#013220")

st.write("")

choices_af_bg_colour = st.color_picker(label = "IV. Choose the colour for after selection choices background :-", value = "#668479")

st.write("")

ranking_light_bg_colour = st.color_picker(label = "V. Choose the light colour for ranking background :-", value = "#013220")

st.write("")

ranking_dark_bg_colour = st.color_picker(label = "VI. Choose the dark colour for ranking background :-", value = "#335A4C")

st.write("")

matrix_choices_colour = st.color_picker(label = "VII. Choose the colour for matrix choices background :-", value = "#013220")

st.write("")

st.markdown("---")

st.write("")

# CEO Light CSS Tempelate

code = f'''

/* Custom Colors */
/* Landing page*/
#o2t-custom-landing-holder {{}}
#o2t-custom-landing-header {{background:none;}}
#o2t-custom-landing-text{{color:#000;}}
#o2t-custom-landing-text .survey-start-btn{{background: {start_button_bg_colour};color:#FFF;}}
.o2t_pageQMS #pageViewer{{background:url({bg_img}) center;background-size: cover;background-color:#FFF;}}
.o2t_pageQMS .STATIC,
.o2t_pageQMS .QUESTION,
.o2t_pageQMS .INPUT,
.o2t_pageQMS .MATRIX {{background:rgba(255,255,255,0.33);}}
.o2t_pageQMS .QUESTION .imageOverlay, 
.o2t_pageQMS .QUESTION .imageUnderlay{{display:none;}}
.o2t_pageQMS .INPUT .imageOverlay, 
.o2t_pageQMS .INPUT .imageUnderlay{{display:none;}}

.o2t_pageQMS .QUESTION [data-role="content"],
.o2t_pageQMS .INPUT [data-role="content"]{{top:50%;transform:translateY(-50%);height:auto;width:60%;margin-left:20%;}}
.o2t_pageQMS .QUESTION .questionOverlay,
.o2t_pageQMS .INPUT .questionOverlay{{display:block;position:relative;padding: 0;}}
.o2t_pageQMS .optionsOverlay{{height:auto;position:relative;display:block;}}
.o2t_pageQMS .QUESTION .middleAlignWrapper,
.o2t_pageQMS .INPUT .middleAlignWrapper{{display:block;padding-bottom:50px;color:#000;}}
.o2t_pageQMS .RATING .optionWrapper img{{max-width:80%;max-height:100%;padding-top:10%}}
.o2t_pageQMS .CHOICES .optionWrapper img{{max-width:50%;max-height:100%;}}
.o2t_pageQMS .CHOICES .optionWrapper .img-sub-text{{padding-top:20px;}}

.o2t_pageQMS .RATING .jsAnswersOverlay .middleAlignWrapper{{display:block;padding-bottom:50px;color:#fff;}}

/*form specific */
.o2t_pageQMS .FORM .matrixQuestioncounter{{top:20%;bottom:unset;}}
.o2t_pageQMS #formScroller .QUESTION [data-role="content"],
.o2t_pageQMS #formScroller .INPUT [data-role="content"]{{top:auto;transform:unset;}}
.o2t_pageQMS #formScroller .formRow [data-duty="query"] .questionOverlay{{padding:0;min-height:auto;padding-top:50px;}}
.o2t_pageQMS #formScroller .formRow.stepFixedHeight [data-duty="query"] .optionsOverlay{{min-height:auto;}}
.o2t_pageQMS #formScroller .optionsOverlay .questionOverlay .mandatorySign{{display:none;}}
.o2t_pageQMS #formScroller .topAlignWrapper{{padding-top:0;}}
.o2t_pageQMS .FORM .questionOverlay{{background:rgba(255,255,255,0.33);color:#000;}}
.o2t_pageQMS .FORM .optionsOverlay .questionOverlay{{background:none}}
.o2t_pageQMS .FORM .optionsOverlay {{background:rgba(255,255,255,0.33)}}
.o2t_pageQMS .FORM .optionsOverlay .optionsOverlay {{background:none}}
.o2t_pageQMS .FORM .formRow textarea{{border:1px solid rgba(0,0,0,0.1)}}
.formFooter{{display:none;}}

.o2t_pageQMS .MATRIX .middleAlignWrapper{{color:#000;}}
.o2t_pageQMS .matrixQuestioncounter{{top:unset;bottom:20%;}}

.pagingControl.pagingControl_with_text{{border:none;background:none;color:#467095;font-size:7vmin;padding:0;}}
.pagingControl.pagingControl_with_text:hover{{color:#000;transition:.5s all;}}
.pos_nextPage, .pos_skipPage{{top:50px;right:25px;}}
.pos_prevPage{{top:50px;left:25px;}}

.o2t_pageQMS .optionsOverlay .horizontalList{{display:flex;flex-direction:row;justify-content: space-evenly;}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList .horizontalListItem{{position:relative;padding:0!important;filter: brightness(1)!important;margin:1px;transition:.5s all;height:unset;align-items:center;}}
.o2t_pageQMS .CHOICES .optionsOverlay .horizontalList .horizontalListItem{{position:relative;padding:0!important;filter: brightness(1)!important;margin:1px;background:{choices_bg_colour};transition:.5s all;height:unset;align-items:center;width:100%!important;}}
.o2t_pageQMS .optionsOverlay .horizontalList.optionsCol11deep .horizontalListItem{{position:relative;padding:0!important;filter: brightness(1)!important;margin:1px;transition:.5s all;height:unset;align-items:center;}}
.o2t_pageQMS .optionsOverlay .horizontalList .horizontalListItem:hover{{box-shadow: 0 5px 11px 0 rgba(0,0,0,0.33), 0 4px 15px 0 rgba(0,0,0,0.33);}}
.o2t_pageQMS .optionsOverlay .horizontalList .horizontalListItem.jsAnswerToStore{{box-shadow: 0 5px 11px 0 rgba(0,0,0,0.33), 0 4px 15px 0 rgba(0,0,0,0.33);}}
.o2t_pageQMS .optionWrapper{{padding:20px 0;font-weight:100;}}
.o2t_pageQMS .INPUT .optionsOverlay .horizontalList .horizontalListItem{{background:none;}}
.o2t_pageQMS .INPUT .optionsOverlay .horizontalList .horizontalListItem:hover{{box-shadow:none;}}
.o2t_pageQMS .INPUT textarea, .o2t_pageQMS .INPUT input {{width:100%!important;font-family:'ProximaNova';font-size:3.5vmin;padding:0;border: 1px solid rgba(0,0,0,0.1);background:rgba(255,255,255,0.8);color:#000;padding:5px;}}
.o2t_pageQMS .OPEN .has-validation:focus, .o2t_pageQMS .OPEN .has-validation.focus{{border:1px solid rgba(0,0,0,0.15);}}
.o2t_pageQMS .OPEN .has-validation.is-valid:focus, .o2t_pageQMS .OPEN .has-validation.is-valid.focus{{border:1px solid green;}}
.o2t_pageQMS .OPEN .has-validation.is-wrong:focus, .o2t_pageQMS .OPEN .has-validation.is-wrong.focus{{border:1px solid red;}}
.o2t_pageQMS .OPEN .has-validation.is-invalid:focus, .o2t_pageQMS .OPEN .has-validation.is-invalid.focus{{border:1px solid orange;}}
.o2t_pageQMS .INPUT textarea::placeholder, .o2t_pageQMS .INPUT input::placeholder {{color:#000;}}

.o2t_pageQMS .optionsOverlay .horizontalList .optionColor0.jsAnswerToStore{{background:#690000;}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor1.jsAnswerToStore{{background:#991517;}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor2.jsAnswerToStore{{background:#c6151f}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor3.jsAnswerToStore{{background:#ef2a21}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor4.jsAnswerToStore{{background:#f46f19}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor5.jsAnswerToStore{{background:#f4b90c}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor6.jsAnswerToStore{{background:#f4e100}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor7.jsAnswerToStore{{background:#b9e000}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor8.jsAnswerToStore{{background:#6fd900}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor9.jsAnswerToStore{{background:#46ba00}}
.o2t_pageQMS .optionsOverlay .horizontalList .optionColor10.jsAnswerToStore{{background:#2b8e0a}}

.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor0{{background:#690000;}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor1{{background:#991517;}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor2{{background:#c6151f}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor3{{background:#ef2a21}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor4{{background:#f46f19}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor5{{background:#f4b90c}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor6{{background:#f4e100}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor7{{background:#b9e000}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor8{{background:#6fd900}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor9{{background:#46ba00}}
.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol11deep .optionColor10{{background:#2b8e0a}}

/* Ranking */
.o2t_pageQMS .RANKING .optionWrapper .leftIcon{{display:none;}}
.o2t_pageQMS .RANKING .optionWrapper .rankNumber{{color:#FFF!important;width:calc(5% - 10px);text-align:left;padding-left:10px;}}
.o2t_pageQMS .RANKING .optionLightColor.jsAnswerToStore {{ background-color: {ranking_light_bg_colour}!important; color:#FFF;}}
.o2t_pageQMS .RANKING .optionDarkColor.jsAnswerToStore {{ background-color: {ranking_dark_bg_colour}!important; color:#FFF;}}
.o2t_pageQMS .RANKING .optionsOverlay .verticalListItem{{margin:1px 0;}}
.o2t_pageQMS .RANKING .optionWrapper{{padding: 10px 0;}}
.o2t_pageQMS .RANKING .optionWrapper div{{display:block;}}

/* Answer options */
.o2t_pageQMS .optionLightColor {{color:#FFF;}}
.o2t_pageQMS .optionDarkColor {{color:#FFF;}}
.o2t_pageQMS .optionLightColor.jsAnswerToStore {{ background-color: {choices_af_bg_colour}!important; color:#FFF;}}
.o2t_pageQMS .optionDarkColor.jsAnswerToStore {{ background-color: {choices_af_bg_colour}!important; color:#FFF;}}

@media only screen and (max-width: 896px){{
	.o2t_pageQMS .QUESTION [data-role="content"],
	.o2t_pageQMS .INPUT [data-role="content"]{{top:50%;transform:translateY(-50%);height:auto;width:95%;margin-left:2.5%;}}
	.pos_nextPage, .pos_skipPage{{top:10px;right:5px;}}
	.pos_prevPage{{top:10px;left:5px;}}
	.o2t_pageQMS .CHOICES .optionWrapper img{{max-width:25%;max-height:100%;}}
	.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol4deep .horizontalListItem{{width:75px!important;height:75px;}}
	.o2t_pageQMS .RATING .optionsOverlay .horizontalList.optionsCol5deep .horizontalListItem{{width:75px!important;height:75px;}}
	.o2t_pageQMS .mainText{{font-size:7vmin;line-height:7.5vmin;font-weight:100;}}
	.o2t_pageQMS .subText{{font-size:5.5vmin!important;line-height:6.5vmin!important;font-weight:100;}}
	.o2t_pageQMS .optionsOverlay{{font-size:5.5vmin!important;line-height:5.5vmin!important;font-weight:100;}}
	.o2t_pageQMS .INPUT textarea, .o2t_pageQMS .INPUT input{{font-size:5.5vmin!important;line-height:5.5vmin!important;font-weight:100;}}
	.o2t_pageQMS .CHOICES .optionWrapper .img-sub-text{{padding-top:5px;}}
}}

@media only screen and (max-width: 896px) and (orientation: portrait){{
	.o2t_pageQMS .CHOICES .optionWrapper img{{max-width:10%;max-height:100%;}}
	.o2t_pageQMS .optionsOverlay .horizontalList{{display:flex;flex-direction:column;}}
	.o2t_pageQMS .RATING .optionsOverlay .horizontalList{{display:flex;flex-direction:row;}}
}}

/* Matrix */
.o2t_pageQMS .matrixOverlay .horizontalList .horizontalListItem{{background: {matrix_choices_colour};}}



/* DEFAULT STYLES DON'T TOUCH */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700');

/* LANDING */
#o2t-custom-landing-holder{{position:fixed;top:0;left:0;width:100%;height:100%;background-size:cover;}}
#o2t-custom-landing-header{{position:absolute;top:0;left:0;width:100%;height:130px;text-align:center;}}
#o2t-custom-landing-header img{{position:absolute;left:50%;top:25px;max-height:80px;    transform: translateX(-50%);}}
#o2t-custom-landing-text{{position:absolute;top:50%;left:50%;transform:translateX(-50%) translateY(-50%);width:750px;max-width:90%;text-align:center;font-family: 'Roboto', sans-serif;padding:50px 25px;}}
#o2t-custom-landing-text .survey-title{{font-size: 4rem;line-height:4rem;font-weight:400;}}
#o2t-custom-landing-text .survey-intro{{font-size: 3vmin;line-height:4vmin;font-weight:300;padding: 25px 0 50px 0;}}
#o2t-custom-landing-text .survey-start-btn{{font-size: 2rem;font-weight:400;text-transform: uppercase;padding: .84rem 2.14rem;display: inline-block;border-radius:510em;transition: .5s ease;cursor:pointer;}}
#o2t-custom-landing-text .survey-start-btn:hover{{box-shadow: 0 5px 11px 0 rgba(0,0,0,0.18), 0 4px 15px 0 rgba(0,0,0,0.15);}}

@media only screen and (max-width: 896px){{
	#o2t-custom-landing-header{{height:60px;}}
	#o2t-custom-landing-header img{{position:absolute;left:50%;top:10px;max-height:40px;    transform: translateX(-50%);}}
}}

/* QUESTIONS */
.o2t_pageQMS .imageUnderlay {{ background-size:cover;}}
.o2t_pageQMS .questionOverlay {{ background:none; }}
input,textarea {{max-width:100%;}}


/* MATRIX */
#matrixScroller{{overflow-y: scroll;}}
.o2t_pageQMS .MATRIX .questionOverlay {{ background:none; }}
.o2t_pageQMS .MATRIX .matrixRow .matrixMainText {{border:none;background:none;}}
.o2t_pageQMS .MATRIX .matrixRow .matrixMainText div{{font-size:2.5vmin!important;line-height:1;padding-left:10px;font-weight: 100;}}
.o2t_pageQMS .matrixOverlay .horizontalList .horizontalListItem{{font-size: 2.5vmin;margin: 5px;padding: 0!important;border: none!important;}}
.o2t_pageQMS .MATRIX .optionWrapper {{position:inherit;top:0;}}
.o2t_pageQMS .matrixOverlay .horizontalList .horizontalListItem img {{width: auto!important;height: 60px!important;}}
.o2t_pageQMS .MATRIX .matrixRow {{height:unset;background:rgba(255,255,255,0.9);margin: 3px 5% 1px 5%;border-bottom: 1px solid rgba(0,0,0,0.1);padding-bottom: 3px;}}
.o2t_pageQMS .MATRIX .matrixRow .row{{height:unset;display:flex;flex-direction:row;align-items:center;}}
.o2t_pageQMS .MATRIX .matrixRow .matrixMainText, 
.o2t_pageQMS .MATRIX .matrixRow .matrixOptions{{display:flex;flex-direction: row;align-items: center; height: unset;}}
.o2t_pageQMS .matrixOverlay .horizontalList .horizontalListItem{{margin:0 1px;width:100%!important;height:unset;}}
.o2t_pageQMS .matrixOverlay .horizontalList .horizontalListItem:hover{{box-shadow: 0 5px 11px 0 rgba(0,0,0,0.33), 0 4px 15px 0 rgba(0,0,0,0.33);}}
.o2t_pageQMS .matrixOverlay .horizontalList .horizontalListItem.jsAnswerToStore{{box-shadow: 0 5px 11px 0 rgba(0,0,0,0.33), 0 4px 15px 0 rgba(0,0,0,0.33);}}

.o2t_pageQMS .matrixOverlay .horizontalList .optionColor1.jsAnswerToStore{{background:#991517}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor2.jsAnswerToStore{{background:#c6151f}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor3.jsAnswerToStore{{background:#ef2a21}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor4.jsAnswerToStore{{background:#f46f19}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor5.jsAnswerToStore{{background:#f4b90c}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor6.jsAnswerToStore{{background:#f4e100}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor7.jsAnswerToStore{{background:#b9e000}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor8.jsAnswerToStore{{background:#6fd900}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor9.jsAnswerToStore{{background:#46ba00}}
.o2t_pageQMS .matrixOverlay .horizontalList .optionColor10.jsAnswerToStore{{background:#2b8e0a}}

@media only screen and (max-width: 896px){{
    .o2t_pageQMS .MATRIX .matrixRow {{margin:20px 2.5%;}}
    .o2t_pageQMS .MATRIX .matrixRow .row{{flex-direction: column;}}
    .o2t_pageQMS .matrixOverlay{{font-size:2rem;line-height:2rem;}}
    .o2t_pageQMS .matrixOverlay .horizontalList .horizontalListItem{{margin:1px;}}
    .o2t_pageQMS .matrixOverlay .horizontalList .horizontalListItem img {{width: auto!important;}}
    .o2t_pageQMS .MATRIX .matrixRow .matrixMainText div{{font-size:6.5vmin!important;padding:10px;font-weight: 100;text-align:center;}}
    .o2t_pageQMS .MATRIX.RATING-PAGE .matrixOverlay .horizontalList{{min-height:50px;}}
    .o2t_pageQMS .RATING-PAGE .optionWrapper{{font-size:5.5vmin}}
}}

@media only screen and (max-width: 896px) and (orientation: landscape){{
	 .o2t_pageQMS .MATRIX .matrixRow .matrixMainText div{{text-align:left;}}
    .o2t_pageQMS .MATRIX .matrixRow .row{{flex-direction: row;}}
	 .o2t_pageQMS .MATRIX .matrixRow {{margin:5px 2.5%;}}

}}

/* DRAGGABLE */
.o2t_pageQMS .DRAGGING .optionsOverlay .optionWrapper{{padding:3px;font-size:0.7em;}}


'''



st.download_button("Download CSS Text", code, "CSS Text", mime = "text/plain")