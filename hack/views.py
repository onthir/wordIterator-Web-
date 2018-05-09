from django.shortcuts import render
import math
import itertools 
# Create your views here.

words = []
result = []
results = []
def home(request):
    # clear the list on each 
    del(words[:])
    del(result[:])
    del(results[:])

    word = request.GET.get('scrambled')
    choice = request.GET.get('select')
    if word:
        comb = math.factorial(len(word))

        length = len(word)
        # create all possible combinations
        for word in itertools.permutations(word):
            a = (''.join(word))
            words.append(a)

        length = len(word)
        for i in range(len(word)):
            for x in words:
                d = (x[:length])
                if not d in results:
                    results.append(d)
                else:
                    pass
                if not d in result:
                    result.append(d)
            length -=1
        context = {
            'comb': comb,
            'results': results
        }
        return render(request, 'hack/index.html', context)
    else:
        return render(request, 'hack/index.html')

# def check_real(request):
#     del(results[:])
#     d = enchant.Dict("en_US")
#     for r in result:
#         if (enchant.Dict("en_US").check(r)) == True and len(r) != 1:
#             results.append(r)
#         else:
#             pass
#     return render(request, 'hack/index.html', {'results':results})