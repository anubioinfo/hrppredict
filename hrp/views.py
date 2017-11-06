from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf import settings
# two directional HRP prediction tool [Weeks of pregnancy, age, hb_level, bp_systolic, bp_diastolic]
import pandas as pd
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


# Create your views here.
class HrpPredict(TemplateView):
    def get(self, request):
        #dataparam = request.GET['q']
        data = settings.HIGH_BP
        dataparam = request.GET.get('q', data)

        #return render(request, 'index.html', {'html_table': html_table, 'name': 'Anurag', 'param':dataparam})

        return HttpResponse(dataparam)

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


# To take anc data from user
def add_anc_data(request):
    if request.method == "POST":

        # Assigning posted data
        data={}
        data['weeks_of_preg'] = int(request.POST.get('weeks', 0))
        data['age'] = int(request.POST.get('age', 28))
        data['hb'] = int(request.POST.get('hb', 8))
        data['bp_systolic'] = int(request.POST.get('systolic', 120))
        data['bp_diastolic'] = int(request.POST.get('diastolic', 80))
        predict = predictHRP(data)
        data['predict'] = predict

        # Text message based on prediction
        if(predict == 'hrp'):
            data['p_text'] = settings.HRP
        else:
            data['p_text'] = settings.NORMAL

        # Sending high bp remedies if her BP is higher than usual
        if(data['bp_systolic'] > 140 or data['bp_diastolic'] > 90):
            data['high_bp_text'] = settings.HIGH_BP
        else:
            data['high_bp_text'] = ''

        if(data['hb'] < 7):
            data['low_hb_text'] = settings.LOW_HB
        else:
            data['low_hb_text'] = ''

        return render(request, 'view_anc_data.html', context=data)
    else:
        return render(request, 'add_anc_data.html')


def predictHRP(inputdata):
    data = pd.read_csv('/var/www/html/hrppredict/hrp/static/hrp/data/hrp_data_complex.csv')
    hrpdata = data.values
    # HRP numeric data
    X = hrpdata[:, 1:6]

    # Label of HRP numeric data
    Y = hrpdata[:, 0:1]
    html_table = data.to_html

    validation_size = 0.20
    seed = 7

    # Extracting test and training set
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                    random_state=seed)

    # [Weeks of pregnancy, age, hb_level(<7), bp_systolic (>140), bp_diastolic(>90)]
    X_validation = [[inputdata['weeks_of_preg'], inputdata['age'], inputdata['hb'], inputdata['bp_systolic'], inputdata['bp_diastolic']]]

    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'
    Y_train = Y_train.ravel()

    # Predict the result
    knn = KNeighborsClassifier()

    knn.fit(X_train, Y_train.ravel())

    predictions = knn.predict(X_validation)
    return predictions[0]
