# Fitbit Q&A

## How is my sleep score calculated in the Fitbit app?

Your overall sleep score is a sum of your individual scores in sleep duration, sleep quality, and restoration, for a total score of up to 100. Most people get a score between 72 and 83. Sleep score ranges are:

- Excellent: 90-100
- Good: 80-89
- Fair: 60-79
- Poor: Less than 60

- Duration: Time asleep and awake	How much you slept. The more you sleep, the better your score.
- Quality: Deep and REM sleep	How much time you spent in deep and REM sleep. The more time you spend in these sleep stages, the better your score.
- Restoration: Sleeping heart rate and restlessness	How relaxed you were during sleep. A high sleeping heart rate or too much tossing and turning lowers your score.

## What's my sleeping heart rate in the Fitbit app?

Your sleeping heart rate, which is your heart rate while you’re asleep, is often lower than your resting heart rate. For more information about resting heart rate, see How do I track heart rate with my Fitbit device? Factors such as caffeine, alcohol, stress, illness, or other actions can impact your sleeping heart rate (source).

## What's the difference between resting heart rate and sleeping heart rate?

Your resting heart rate is the number of times your heart beats per minute when you are still and well-rested. Your resting heart rate is estimated each day. Your sleeping heart rate is detected continuously throughout the night.

# Paper highlights

## Paper: A systematic review on automatic identification of insomnia

- "The reason for chronic insomnia, however, is more complicated and calls for a more strategic approach because it may be either physical or psychological"
- "Insomnia that lasts more than a month or at least three nights per week is often referred to as chronic insomnia which is further classified as primary or secondary"
- "Insomnia with a psychological cause is referred to as primary insomnia"
- "A medical or psychological condition results in secondary insomnia (SI). Medical conditions including cancer, lung illness, hypertension, etc. can all contributeto SI. Secondary insomnia can also be brought on by mood and worry"
- "As a result, scientists have begun to develop automatic detection methods for insomnia that rely on physiological cues, yet there is currently no definite test to identify insomnia [36]"

## Paper: A machine learning model for multi-night actigraphic detection of chronic insomnia: development and validation of a pre-screening tool

- "When individuals do seek medical attention, many primary care providers are unsure of how to diagnose insomnia."
- "Actigraphy is a non-invasive method for monitoring human rest/activity patterns."
- "Actigraphy is a non-invasive method for monitoring human rest/activity patterns. Actigraphs can infer sleep characteristics from the motor activity and are widely used to measure sleep in the home environment, including individuals with insomnia [14–16]."
- "However, actigraphy is currently not able to reliably distinguish those with insomnia from healthy sleepers, and thus cannot currently play the screening role suggested above"
- "we have reported a machine learning-based model for the detection and classification of acute insomnia using wrist-actigraphy [17]"
- "From the analysis reported in [17], we found that our model was able to deduce the signatures of acute insomnia from the wrist-worn actigraphy devices with seven nights of data."
- "The criteria for insomnia disorder were established according to the Duke Structured Interview for Sleep Disorders (DSISD) in individuals experiencing insomnia [23]."
- "In total, this study comprised 80 adults; 40 healthy controls and 40 subjects with CI. The two groups were matched on age because of the partner status. The current study used wrist-actigraphy in recruited subjects and the data were collected for one week using actiwatch model Respironics Actiwatch Spectrum Pro and raw data processed with Actiware software (Respironics, Bend, OR, USA). Movement counts were sampled in 60 s epochs. All recruited subjects wore the devices at all times during day and night. All subjects were free to move and were not prohibited from doing any activities of daily living. The data collection for each participant included five working days and one weekend. The participants were not restricted on which specific day of the week to start the measurements."
- "Only the subjects’ nocturnal actigraphy signals, corresponding to the time in bed (TIB), were used for feature extraction."
- "Rather, the start and end of the night were determined automatically by the actigraphy software."
- "Therefore, in this study, we have used ActiWatch-generated rest intervals as TIB."
- "In this study, we employed four different wake limits (intensity filters (InF)) of zero, low, medium and high activity counts of 0, 20, 40 and 80, respectively, on the nocturnal actigraphy signal."
- "We extracted linear and nonlinear features from the nocturnal actigraphy signal such as mean, standard deviation, Poincaré plot features, and entropy-derived measure (sample entropy SampEn). In addition, features such as total sleep time (TST), sleep latency (SL), wake after sleep onset (WASO), sleep–wake ratio (SWR) and sleep efficiency (SE) were also extracted from the nocturnal actigraphy signal."
- "TST (total sleep time) is the total duration of all sleep epochs (activity count is zero) starting from the SO (sleep onset) time."
- "The SO time is defined as the start of the first 10 min epoch of continuous inactivity (activity count is zero) in the nocturnal actigraphy signal."
- "SL is defined as the duration between sleep onset SO and the start time of nocturnal recording."
- "WASO is the period, measured in minutes, by summing all wake epochs in the nocturnal actigraphy signal following the SO time."
- "The ratio of TST and WASO is called SWR (sleep–wake ratio)"
- "The ratio of TST and rest interval, TIB (the rest interval generated by the actiwatch), known as SE (sleep efficiency) or % sleep"
- "In this study, a novel two-layered automated model was employed for detecting individuals with CI"
- "The first layer of the model works by predicting the night labels for all the subjects."
- "In order to avoid the use of the sleep diaries, we labelled each night of data from healthy sleepers as a 'good night of sleep' and that of the CI individuals as a 'bad night of sleep', respectively."
- "The produced night labels were then used to train a supervised classifier to predict the night labels for the test subject during the cross-validation process."
- "Two supervised models of machine learning, namely support vector machine (SVM) and random forests (RF), were used to construct the prediction model. Given a relatively small amount of data, not sufficient for deep learning algorithms to function properly, and the requirement for basic explainability for the models we create, we use these traditional methods"
- "The frequency of bad nights (predicted at layer 1 by the ML model) is used as a criterion for individual classification in the second layer of the model."
- "A threshold value for the number of bad nights to be classified as an individual with CI was determined for each subject."
- "This research uses seven nights of nocturnal actigraphy data for developing a machine learning-based model for automated detection and differentiation of individuals with CI from their healthy partners."
- "A two-layered model is developed, where the first layer predicts the quality of night sleep and classifies it into good or bad night sleep. A second optimizer layer uses the predicted quality of sleep (good/bad) to assign the individual to the CI or healthy group."
- "A leave-one-out validation approach was used to determine the optimal night threshold Th, ensuring that the test subject is not a part of the learning process. To understand the night threshold (Th) use, let us assume a model generated an optimal night threshold of Th = x. If for an individual, the Layer 1 of the model predicted greater than or equal to x nights of the total monitoring nights as  ad nights, he/she would be classified into the CI group"
- "Figure 5 shows the optimal night threshold Th value for the RF classifier. The learned thresholds for both RF and SVM classifier are four nights, respectively, for all iterations of the learning. Table 5 shows the overall model classification performance using the optimal night threshold."

## Paper: Automated Method for Detecting Acute Insomnia Using Multi-Night Actigraphy Data

- "In this paper, we will develop a machine learning model using multi-night actigraphy data for classifying acute insomnia."
- "Seven nights of nocturnal actigraphy data have been used to develop a model for classifying sleep quality into good and bad sleep nights."
- "Nocturnal actigraphy for each subject is labelled based on information derived from actigraphy data rather than using a sleep diary. Thus, the proposed method is only dependent on the actigraphy data."
- "To the best of our knowledge, this is the first machine learning model developed using only the actigraphy data to assess acute insomnia."
- "Our analysis uses actigraphy time series data from a publicly available data source of the publication [13]"
- "This study comprised 45 young adults (age: 18-40 years), including 24 asymptomatic controls (age: 28  6 years) and 21 acute insomnia subjects (age: 25  6 years). The control cohort was composed of self-declared healthy populations with no known problem with sleeping and the insomnia cohort (clinically assessed) did not have any known comorbidity. All subjects were requested to remain in bed between 10pm and 8am next day."
- "The data were pre-processed and prepared for feature extraction. Only nocturnal actigraphy was used to extract features. The nocturnal period analysed in this study is 10pm to 8am (inclusive), since subjects were requested to be in bed during this period in this study."
- "In this study, we empirically selected the Time In Bed (TIB) as 10 hours (10pm to 8am) for all subjects, which determines the length of nocturnal actigraphy data. (Note, the design of the experiment required participants to stay in bed for this period of time). The following sleep features such as Total Sleep Time (TST), Wake After Sleep Onset (WASO) and Sleep-Wake Ratio (SWR) were determined from the nocturnal actigraphy signal."
- "In this study, we have proposed a two-layered model for acute insomnia detection. Layer 1: Machine Learning Model for good or bad night classification. Layer 2: Determining Optimal Threshold (number of nights) for individual (acute or healthy) classification. In the second layer of the model (Figure 1), the frequency of bad nights (predicted by the ML model at layer 1) is used as a feature for individual classification."
- "This study uses the 7-night of actigraphy data for automatic detection of acute insomnia subject using machine learning models."
- "A two-level model is developed to detect acute insomnia, where at the first level quality of sleep (good or bad) is predicted and at the second level, a threshold on seven nights is used to classify the subjects into acute insomnia and healthy groups."
- "Our study appears to be first in detecting acute insomnia using only the actigraphy data."
- "Figure 4 shows the results on subjects with different Th values on night labels provided by SVM and RF (from the layer one of the proposed model), respectively. The balanced performance (sensitivity, specifscity and accuracy are equal) was obtained at 2  Th  3 and 3  Th  4 for the SVM and RF model outcome at layer 1, respectively. This provides a better insight to build a model with an expected level of sensitivity or specicity."

# GPT Questions

>> "idealmente, quantos ciclos de sono profundo um idoso tem por noite"

O sono profundo, ou sono de ondas lentas (fase N3 do sono não-REM), tende a diminuir com a idade. No entanto, é ideal que um idoso consiga alcançar pelo menos um ou dois ciclos de sono profundo por noite. Em termos de duração, isso geralmente equivale a aproximadamente 10  20% do total do sono noturno.

Para um idoso que dorme cerca de 7-8 horas por noite, isso significa que o sono profundo pode representar aproximadamente 42-96 minutos (10% - 22%). É importante lembrar que a quantidade de sono profundo pode variar significativamente de uma pessoa para outra, e a qualidade do sono é tão importante quanto a quantidade. Manter uma boa higiene do sono, como ter uma rotina de sono consistente, evitar cafeína e telas antes de dormir, e manter um ambiente de sono confortável, pode ajudar a melhorar a qualidade do sono profundo.

>> "idealmente, quantos ciclos de sono REM um idoso tem por noite"

Ciclos de Sono REM em Idosos
- Duração dos Ciclos: Cada ciclo de sono completo (incluindo fases não-REM e REM) dura aproximadamente 90 a 120 minutos.
- Número de Ciclos: Durante uma noite de sono de 7-8 horas, uma pessoa geralmente passa por 4 a 5 ciclos completos de sono. Isso inclui períodos de sono REM.
- Proporção de Sono REM: O sono REM geralmente representa cerca de 20-25% do total do sono noturno em adultos jovens. Em idosos, essa proporção pode diminuir ligeiramente, mas muitos ainda conseguem alcançar cerca de 15-20% de sono REM.
- Ciclos de Sono REM: Portanto, idealmente, um idoso pode ter 4 a 5 períodos de sono REM por noite, embora a duração e a intensidade desses períodos possam ser menores em comparação com adultos mais jovens.

"em termos proporcionais, qual o HEART RATE BELOW RESTING ideal para idosos  por noite"

Em resumo, não há um número específico de "HEART RATE BELOW RESTING" considerado ideal para idosos por noite, mas manter a frequência cardíaca em repouso dentro da faixa normal para a idade e o estado de saúde individual é um bom indicador de saúde cardiovascular. 60 a 100 batimentos por minuto.

>> "idealmente, qual a hora de dormir e acordar para um idoso"

Hora de Dormir: Entre 21:00 e 22:00: Muitos idosos se beneficiam de ir para a cama entre 21:00 e 22:00, o que permite que eles aproveitem o ritmo circadiano natural e evitem ficar acordados tarde demais.

Hora de Acordar: Entre 5:00 e 6:00: Se um idoso vai dormir entre 21:00 e 22:00 e dorme por 7-8 horas, o horário ideal para acordar seria entre 5:00 e 6:00.

>> "como diferenciar isonia cronia e aguda"

Insônia Aguda
- Duração: Curta, geralmente menos de três meses.
- Causa: Normalmente relacionada a eventos estressantes ou mudanças na vida, como a perda de um ente querido, um novo emprego, problemas de saúde temporários ou preocupações imediatas.
- Sintomas: Dificuldade temporária em adormecer ou manter o sono, que resolve quando o evento estressante passa ou a pessoa se adapta às mudanças.
- Tratamento: Muitas vezes, medidas de higiene do sono, técnicas de relaxamento e, ocasionalmente, o uso de medicamentos para o sono de curto prazo.

Insônia Crônica
- Duração: Persistente, ocorrendo pelo menos três vezes por semana e durando três meses ou mais.
- Causa: Pode ser multifatorial, incluindo problemas de saúde subjacentes (como distúrbios respiratórios do sono, dores crônicas, doenças neurológicas), condições psicológicas (como ansiedade e depressão), ou hábitos de sono inadequados.
- Sintomas: Dificuldade em adormecer, acordar várias vezes durante a noite, acordar cedo demais e não conseguir voltar a dormir, e sensação de cansaço ou fadiga durante o dia.
- Tratamento: Envolve uma abordagem mais abrangente, incluindo terapia cognitivo-comportamental para insônia (TCC-I), mudanças no estilo de vida, tratamento de condições médicas subjacentes e, em alguns casos, medicamentos.

Considerações Gerais
-  Diagnóstico: A diferenciação entre insônia aguda e crônica é baseada principalmente na duração dos sintomas e na frequência com que ocorrem. Um profissional de saúde pode usar questionários, diários do sono e, em alguns casos, estudos do sono para ajudar a diagnosticar o tipo de insônia.
-  Impacto: Ambas as formas de insônia podem impactar significativamente a qualidade de vida, mas a insônia crônica geralmente tem um impacto mais profundo e duradouro na saúde física e mental.

# Links

- https://blog.fitbit.com/sleep-stages-explained/
- https://support.google.com/fitbit/answer/14236513
- https://www.kaggle.com/datasets/riinuanslan/sleep-data-from-fitbit-tracker/data
