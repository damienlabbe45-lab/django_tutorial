2.2.3
Voyez-vous tous les attributs de vos classes ?

il faut cliquer pour voir tout les attributs de questions et de votes

Pouvez-vous filtrer vos données suivants tous les attributs ? 

non on ne peut pas.

Pouvez-vous trier vos données suivants tous les attributs ? 

on peut pas trier

Pouvez-vous chercher un contenu parmi tous les champs ? 

on peut pas chercher un contenu ou un caractère.

2.2.4.5
Déconnectez-vous et essayer de vous reconnecter avec ce 
nouveau compte. Y parvenez-vous ? 

Je n'y parvient pas

2.2.2.2

1

print(Question.objects.all())
<QuerySet [<Question: Quoi de neuf ?>, <Question: Django est-il une usine à gaz?>, <Question: Django a t'il du code legacy ?>, <Question: Django devrais t- il supprimer ses commandes?>, <Question: quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande?>, <Question: devrais-t-on supprimmer Django?>, <Question: Django est-il à l'image des politiciens ?>]>
>>> type(Question.objects.all())
<class 'django.db.models.query.QuerySet'>
>>> dir(Question.objects.all()[0])
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_composite_pk', '_check_constraints', '_check_db_table_comment', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references', '_get_field_expression_map', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_is_pk_set', '_meta', '_parse_save_params', '_perform_date_checks', '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val', '_state', '_validate_force_insert', 'adelete', 'arefresh_from_db', 'asave', 'check', 'choice_set', 'clean', 'clean_fields', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_constraints', 'get_deferred_fields', 'get_next_by_pub_date', 'get_previous_by_pub_date', 'id', 'objects', 'pk', 'prepare_database_save', 'pub_date', 'question_text', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_constraints', 'validate_unique', 'was_published_recently']
>>> Question.objects.all()[0].__dict__
{'_state': <django.db.models.base.ModelState object at 0x000001A621696150>, 'id': 1, 'question_text': 'Quoi de neuf ?', 'pub_date': datetime.datetime(2026, 11, 2, 13, 55, 11, tzinfo=datetime.timezone.utc)}
>>> listQuestionstr : list[str] = [ f"{question.id} {question.question_text} {question.pub_date} \n" for question in Question.objects.all()]
>>> listQuestionstr
['1 Quoi de neuf ? 2026-11-02 13:55:11+00:00 \n', '2 Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00 \n', "3 Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00 \n", '4 Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00 \n', "5 quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00 \n", '6 devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00 \n', "7 Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00 \n"]
>>> print("".join(listQuestionstr)
... )
1 Quoi de neuf ? 2026-11-02 13:55:11+00:00
2 Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00
3 Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00
4 Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00
5 quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00
6 devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00
7 Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00

>>> print(str(listQuestionstr).replace('\\n', '\n'))
['1 Quoi de neuf ? 2026-11-02 13:55:11+00:00
', '2 Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00
', "3 Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00
", '4 Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00
', "5 quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00
", '6 devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00
', "7 Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00
"]


2

from django.utils import timezone
>>> Question.objects.get(pub_date__year=timezone.now().year)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\LabbeD\OneDrive - Facylities Multi Services\Documents\django\html.venv\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "C:\Users\LabbeD\OneDrive - Facylities Multi Services\Documents\django\html.venv\Lib\site-packages\django\db\models\query.py", line 638, in get
    raise self.model.MultipleObjectsReturned(
    ...<5 lines>...
    )
polls.models.Question.MultipleObjectsReturned: get() returned more than one Question -- it returned 3!
>>> Question.objects.filter(pub_date__year=timezone.now().year)
<QuerySet [<Question: Quoi de neuf ?>, <Question: Django est-il une usine à gaz?>, <Question: devrais-t-on supprimmer Django?>]>


3

Question.objects.filter(id = 2)
<QuerySet [<Question: Django est-il une usine à gaz?>]>
 question = Question.objects.filter(id = 2)
>>> question = Question.objects.filter(id = 2)[0]
>>> question
<Question: Django est-il une usine à gaz?>
>>> print(f"{question.id}  {question.question_text} {question.pub_date}")
2  Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00

Choice.objects.filter(question_id= question.id)
<QuerySet [<Choice: Oui il est une énorme usine à gaz avec ses commandes.>, <Choice: oui, il est parfait pour certaines personnes qui adore imiter les anes>, <Choice: oui, aussi sûr et certain qu'on utilise SQLITE3>]>

4

listQuestionstr : list[str] = [ f"{question.id} {question.question_text} {question.pub_date} : {" ".join(Choice.objects.filter(question_id= question.id)} \n" for question in Question.objects.all()]
  File "<console>", line 1
    listQuestionstr : list[str] = [ f"{question.id} {question.question_text} {question.pub_date} : {" ".join(Choice.objects.filter(question_id= question.id)} \n" for question in Question.objects.all()]
                                                                                                                                                            ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> listQuestionstr : list[str] = [ f"{question.id} {question.question_text} {question.pub_date} : {" ".join(Choice.objects.filter(question_id = question.id))} \n" for question in Question.objects.all()]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: sequence item 0: expected str instance, Choice found
>>> listQuestionstr : list[str] = [ f"{question.id} {question.question_text} {question.pub_date} : {" ".join(str(Choice.objects.filter(question_id = question.id)))} \n" for question in Question.objects.all()]
>>> print(lisQuestionstrst)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'lisQuestionstrst' is not defined. Did you mean: 'listQuestionstr'?
>>> print(lisQuestionstr)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'lisQuestionstr' is not defined. Did you mean: 'listQuestionstr'?
>>> print(listQuestionstr)
['1 Quoi de neuf ? 2026-11-02 13:55:11+00:00 : < Q u e r y S e t   [ < C h o i c e :   l e   c i e l   d e   l a   n u i t   e s t   t o m b é   s u r   D j a n g o   e t   i l   e s t   t o m b é   d a n s   l e s   t é n è b r e s > ,   < C h o i c e :   j u s t e   o n   a t t e n d   q u e   l a   m a g i e   d e   d j a n g o   s e   t a r i t > ,   < C h o i c e :   U n e   b r u t e   t o r d s   l e     b o u t   d e   c o d e   d e   d j a n g o   q u i   l u i   s e r t   d e   n e z . > ] > \n', "2 Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00 : < Q u e r y S e t   [ < C h o i c e :   O u i   i l   e s t   u n e   é n o r m e   u s i n e   à   g a z   a v e c   s e s   c o m m a n d e s . > ,   < C h o i c e :   o u i ,   i l   e s t   p a r f a i t   p o u r   c e r t a i n e s   p e r s o n n e s   q u i   a d o r e   i m i t e r   l e s   a n e s > ,   < C h o i c e :   o u i ,   a u s s i   s û r   e t   c e r t a i n   q u ' o n   u t i l i s e   S Q L I T E 3 > ] > \n", "3 Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00 : < Q u e r y S e t   [ < C h o i c e :   O u i   i l   e n   a   é n o r m é m e n t   d a t a n t   d e s   a n n é e s   2 0 0 0   v u   q u e   i l   d a t e   d e   p y t h o n   2 . 7 .     e t   i l   n ' e s t   p a s   n a t i v e m e n t   a s y n c h r o n e .   s e s   c r é a t e u r s   o n t   c o m m e n c é   à   l e   r e n d r e   a s y n c h r o n e . > ,   < C h o i c e :   o u i   i l   e n   a   c o m m e   b o n   n o m b r e   d ' e n t r e p r i s e s   o n t   d u   c o d e   a s s e z   v i e u x . > ,   < C h o i c e :   o u i   e t   t o u t   c o m m e   c o d e   l e g a c y ,   b a h   i l   y   a   s o u v e n t   l e s   v u n é r a b i l i t é s   q u i   v o n t   a v e c   m ê m e   s i   t o u t   c o d e   a v e c   d e s   l a n g a g e s   d e   p r o g g r a m m a t i o n   e n   a . > ] > \n", '4 Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00 : < Q u e r y S e t   [ < C h o i c e :   O u i   à   1 0 0 %   . > ,   < C h o i c e :   O u i   à   1 0 0 0 % > ,   < C h o i c e :   O u i   e t   d e   m a n i è r e   d é f i n i t i v e . > ] > \n', "5 quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00 : < Q u e r y S e t   [ < C h o i c e :   L ' i n t é r è t   e s t   d e   f a i r e   c r o i c r e   q u e   t o u t   e s t   m a g i e   p o u r   m i e u x   n o u s   f a i r e   c r o i c r e   q u e   t o u t   e s t   m a g i e   e t   s u r d i m e n s s i o n n e r   l e s   t a b l e s   d e s   b a s e s   d e   d o n n é e s   p o u r   e n   c r é é   3 9 0 0 0 . > ,   < C h o i c e :   l ' i n t è r e t   e s t   d e   r e n d r e   l e s   g e n s   t o u t   a u s s i   d é p e n d a n t   d e   l u i .   a u   p o i n t   d e   i m p o s e r   s a   d i c t a t u r e > ,   < C h o i c e :   i l   s ' a g i t   d e   j u s t e   s i m p l i f i e r   p o u r   m i e u x   f a i r e   c r o i c r e   q u e   i l   f a u t   3   j o u r s   p o u r   c r é é   u n e   i n t e r f a c e   p a r f a i t e . > ] > \n", "6 devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00 : < Q u e r y S e t   [ < C h o i c e :   a l o r s   l e   s u p p r i m m e r   p e u t - ê t r e   p a s .   l e   r e f a c t o r i s e r   c o m p l è t e m e n t   e t   s u p p r i m m e r   l a   d é p e n d a n c e   à   m a n a g e   o u i   t o u t   e n   g a r d a n t   l e   m o y e n   d e   s ' o c c u p p e r   d e   d é m a r r e r   l e   s e r v e u r > ,   < C h o i c e :   n o n   t o u t   d e   m ê m e   p a s   m a l g r é   t o u t   s e s   d é f a u t s .   m a i s   c o m p l è t e m e n t   l e   c h a n g e r   o u i . > ,   < C h o i c e :   s i   o n   n e   l e   m o d i f i e   p a s .   c a   s e r a   à   e n v i s a g e r . > ] > \n", "7 Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00 : < Q u e r y S e t   [ < C h o i c e :   O u i ,   i l   e s t   à   l ' i m a g e   d ' e u x . > ,   < C h o i c e :   o u i ,   i l   e s t   b i e n   à   l ' i m a g e   q u ' o n   p o u r r a i t   c r o i r e   q u ' i l s   v o n t   d i r e   h i   h a n > ,   < C h o i c e :   O u i ,   o n   p o u r r a i t   s e   d e m a n d e r   s i   c ' e s t   e u x   q u i   l ' o n t   c o d é . > ] > \n"]
>>> listQuestionstr = [
...     f"{q.id} | {q.question_text} | {q.pub_date} -> " + ", ".join(q.choice_set.values_list('choice_text', flat=True))
...     for q in Question.objects.all()
... ]
>>> print(listQuestionstr)
['1 | Quoi de neuf ? | 2026-11-02 13:55:11+00:00 -> le ciel de la nuit est tombé sur Django et il est tombé dans les ténèbres, juste on attend que la magie de django se tarit, Une brute tords le  bout de code de django qui lui sert de nez.', "2 | Django est-il une usine à gaz? | 2026-11-04 22:00:00+00:00 -> Oui il est une énorme usine à gaz avec ses commandes., oui, il est parfait pour certaines personnes qui adore imiter les anes, oui, aussi sûr et certain qu'on utilise SQLITE3", "3 | Django a t'il du code legacy ? | 2027-02-27 00:34:00+00:00 -> Oui il en a énormément datant des années 2000 vu que il date de python 2.7.  et il n'est pas nativement asynchrone. ses créateurs ont commencé à le rendre asynchrone., oui il en a comme bon nombre d'entreprises ont du code assez vieux., oui et tout comme code legacy, bah il y a souvent les vunérabilités qui vont avec même si tout code avec des langages de proggrammation en a.", '4 | Django devrais t- il supprimer ses commandes? | 1997-11-16 23:00:00+00:00 -> Oui à 100% ., Oui à 1000%, Oui et de manière définitive.', "5 | quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? | 2024-09-11 07:56:00+00:00 -> L'intérèt est de faire croicre que tout est magie pour mieux nous faire croicre que tout est magie et surdimenssionner les tables des bases de données pour en créé 39000., l'intèret est de rendre les gens tout aussi dépendant de lui. au point de imposer sa dictature, il s'agit de juste simplifier pour mieux faire croicre que il faut 3 jours pour créé une interface parfaite.", "6 | devrais-t-on supprimmer Django? | 2026-11-02 11:45:00+00:00 -> alors le supprimmer peut-être pas. le refactoriser complètement et supprimmer la dépendance à manage oui tout en gardant le moyen de s'occupper de démarrer le serveur, non tout de même pas malgré tout ses défauts. mais complètement le changer oui., si on ne le modifie pas. ca sera à envisager.", "7 | Django est-il à l'image des politiciens ? | 2234-01-14 14:44:30+00:00 -> Oui, il est à l'image d'eux., oui, il est bien à l'image qu'on pourrait croire qu'ils vont dire hi han, Oui, on pourrait se demander si c'est eux qui l'ont codé."]
>>> listQuestionstr = [f"{q.id}  {q.question_text} {q.pub_date} : " ", ".join(q.choice_set.values_list('choice_text', flat=True)) for q in Question.objects.all()]
>>> print(listQuestionstr)
['le ciel de la nuit est tombé sur Django et il est tombé dans les ténèbres1  Quoi de neuf ? 2026-11-02 13:55:11+00:00 : , juste on attend que la magie de django se tarit1  Quoi de neuf ? 2026-11-02 13:55:11+00:00 : , Une brute tords le  bout de code de django qui lui sert de nez.', "Oui il est une énorme usine à gaz avec ses commandes.2  Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00 : , oui, il est parfait pour certaines personnes qui adore imiter les anes2  Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00 : , oui, aussi sûr et certain qu'on utilise SQLITE3", "Oui il en a énormément datant des années 2000 vu que il date de python 2.7.  et il n'est pas nativement asynchrone. ses créateurs ont commencé à le rendre asynchrone.3  Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00 : , oui il en a comme bon nombre d'entreprises ont du code assez vieux.3  Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00 : , oui et tout comme code legacy, bah il y a souvent les vunérabilités qui vont avec même si tout code avec des langages de proggrammation en a.", 'Oui à 100% .4  Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00 : , Oui à 1000%4  Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00 : , Oui et de manière définitive.', "L'intérèt est de faire croicre que tout est magie pour mieux nous faire croicre que tout est magie et surdimenssionner les tables des bases de données pour en créé 39000.5  quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00 : , l'intèret est de rendre les gens tout aussi dépendant de lui. au point de imposer sa dictature5  quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00 : , il s'agit de juste simplifier pour mieux faire croicre que il faut 3 jours pour créé une interface parfaite.", "alors le supprimmer peut-être pas. le refactoriser complètement et supprimmer la dépendance à manage oui tout en gardant le moyen de s'occupper de démarrer le serveur6  devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00 : , non tout de même pas malgré tout ses défauts. mais complètement le changer oui.6  devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00 : , si on ne le modifie pas. ca sera à envisager.", "Oui, il est à l'image d'eux.7  Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00 : , oui, il est bien à l'image qu'on pourrait croire qu'ils vont dire hi han7  Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00 : , Oui, on pourrait se demander si c'est eux qui l'ont codé."]
>>> listQuestionstr = [f"{q.id} {q.question_text} {q.pub_date} : " + ", ".join(q.choice_set.values_list('choice_text', flat=True)) + "\n" for q in Question.objects.all()]
>>> print(listQuestionstr)
['1 Quoi de neuf ? 2026-11-02 13:55:11+00:00 : le ciel de la nuit est tombé sur Django et il est tombé dans les ténèbres, juste on attend que la magie de django se tarit, Une brute tords le  bout de code de django qui lui sert de nez.\n', "2 Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00 : Oui il est une énorme usine à gaz avec ses commandes., oui, il est parfait pour certaines personnes qui adore imiter les anes, oui, aussi sûr et certain qu'on utilise SQLITE3\n", "3 Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00 : Oui il en a énormément datant des années 2000 vu que il date de python 2.7.  et il n'est pas nativement asynchrone. ses créateurs ont commencé à le rendre asynchrone., oui il en a comme bon nombre d'entreprises ont du code assez vieux., oui et tout comme code legacy, bah il y a souvent les vunérabilités qui vont avec même si tout code avec des langages de proggrammation en a.\n", '4 Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00 : Oui à 100% ., Oui à 1000%, Oui et de manière définitive.\n', "5 quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00 : L'intérèt est de faire croicre que tout est magie pour mieux nous faire croicre que tout est magie et surdimenssionner les tables des bases de données pour en créé 39000., l'intèret est de rendre les gens tout aussi dépendant de lui. au point de imposer sa dictature, il s'agit de juste simplifier pour mieux faire croicre que il faut 3 jours pour créé une interface parfaite.\n", "6 devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00 : alors le supprimmer peut-être pas. le refactoriser complètement et supprimmer la dépendance à manage oui tout en gardant le moyen de s'occupper de démarrer le serveur, non tout de même pas malgré tout ses défauts. mais complètement le changer oui., si on ne le modifie pas. ca sera à envisager.\n", "7 Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00 : Oui, il est à l'image d'eux., oui, il est bien à l'image qu'on pourrait croire qu'ils vont dire hi han, Oui, on pourrait se demander si c'est eux qui l'ont codé.\n"]
>>> print("".join(listQuestionstr))
1 Quoi de neuf ? 2026-11-02 13:55:11+00:00 : le ciel de la nuit est tombé sur Django et il est tombé dans les ténèbres, juste on attend que la magie de django se tarit, Une brute tords le  bout de code de django qui lui sert de nez.
2 Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00 : Oui il est une énorme usine à gaz avec ses commandes., oui, il est parfait pour certaines personnes qui adore imiter les anes, oui, aussi sûr et certain qu'on utilise SQLITE3
3 Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00 : Oui il en a énormément datant des années 2000 vu que il date de python 2.7.  et il n'est pas nativement asynchrone. ses créateurs ont commencé à le rendre asynchrone., oui il en a comme bon nombre d'entreprises ont du code assez vieux., oui et tout comme code legacy, bah il y a souvent les vunérabilités qui vont avec même si tout code avec des langages de proggrammation en a.
4 Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00 : Oui à 100% ., Oui à 1000%, Oui et de manière définitive.
5 quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00 : L'intérèt est de faire croicre que tout est magie pour mieux nous faire croicre que tout est magie et surdimenssionner les tables des bases de données pour en créé 39000., l'intèret est de rendre les gens tout aussi dépendant de lui. au point de imposer sa dictature, il s'agit de juste simplifier pour mieux faire croicre que il faut 3 jours pour créé une interface parfaite.
6 devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00 : alors le supprimmer peut-être pas. le refactoriser complètement et supprimmer la dépendance à manage oui tout en gardant le moyen de s'occupper de démarrer le serveur, non tout de même pas malgré tout ses défauts. mais complètement le changer oui., si on ne le modifie pas. ca sera à envisager.
7 Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00 : Oui, il est à l'image d'eux., oui, il est bien à l'image qu'on pourrait croire qu'ils vont dire hi han, Oui, on pourrait se demander si c'est eux qui l'ont codé.


5

listQuestionstr = [f"{question.id} {question.question_text} {question.pub_date} : " + ", ".join(len(question.choice_set.values_list('choice_text', flat=True))) + "\n" for question in Question.objects.all()]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: can only join an iterable
>>> listQuestionstr = [f"{question.id} {question.question_text} {question.pub_date} : {len(question.choice_set.values_list('choice_text', flat=True))} \n" for question in Question.objects.all()]
>>> print("".join(listQuestionstr))
1 Quoi de neuf ? 2026-11-02 13:55:11+00:00 : 3
2 Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00 : 3
3 Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00 : 3
4 Django devrais t- il supprimer ses commandes? 1997-11-16 23:00:00+00:00 : 3
5 quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande? 2024-09-11 07:56:00+00:00 : 3
6 devrais-t-on supprimmer Django? 2026-11-02 11:45:00+00:00 : 3
7 Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00 : 3


7


Question.objects.all()
<QuerySet [<Question: Quoi de neuf ?>, <Question: Django est-il une usine à gaz?>, <Question: Django a t'il du code legacy ?>, <Question: Django devrais t- il supprimer ses commandes?>, <Question: quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande?>, <Question: devrais-t-on supprimmer Django?>, <Question: Django est-il à l'image des politiciens ?>]>
>>> Question.objects.all(order_by())
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'order_by' is not defined
>>> Question.objects.all(order_by(pub_date))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'order_by' is not defined
>>> Question.objects.all(pub_date.order_by())
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'pub_date' is not defined
>>> Question.objects.all().order_by(-"pub_date")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: bad operand type for unary -: 'str'
>>> Question.objects.all().order_by("-pub_date")
<QuerySet [<Question: Django est-il à l'image des politiciens ?>, <Question: Django a t'il du code legacy ?>, <Question: Django est-il une usine à gaz?>, <Question: Quoi de neuf ?>, <Question: devrais-t-on supprimmer Django?>, <Question: quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande?>, <Question: Django devrais t- il supprimer ses commandes?>]>

9

q = Question(question_text="Faudrait - il lister tout ce qui ne va pas chez Django?", pub_date=timezone.now())
>>> q.save()

10

q.choice_set.create(choice_text="Oui il faut lister en commençant par la gestion du caractère * ", votes=0)
<Choice: Oui il faut lister en commençant par la gestion du caractère * >
>>> q.choice_set.create(choice_text="Oui, il faut aussi le rendre plus modulaire et lui permettre d'importer que si c'est néccessaire et non pas tout", votes=0)
<Choice: Oui, il faut aussi le rendre plus modulaire et lui permettre d'importer que si c'est néccessaire et non pas tout>
>>> q.choice_set.create(choice_text="Oui, il faut commencer à refactoriser et enlever le code legacy quand c'est utile", votes=0)
<Choice: Oui, il faut commencer à refactoriser et enlever le code legacy quand c'est utile>
>>> q.save()

11


listQuestionstr = [f"{question.id} {question.question_text} {question.pub_date} \n" for question in Question.objects.all() if question.was_published_recently()]
>>> print("".join(listQuestionstr))
1 Quoi de neuf ? 2026-11-02 13:55:11+00:00
2 Django est-il une usine à gaz? 2026-11-04 22:00:00+00:00
3 Django a t'il du code legacy ? 2027-02-27 00:34:00+00:00
7 Django est-il à l'image des politiciens ? 2234-01-14 14:44:30+00:00
8 Faudrait - il lister tout ce qui ne va pas chez Django? 2026-11-03 12:44:01.489008+00:00


6

Question.objects.all().order_by("votes")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\LabbeD\OneDrive - Facylities Multi Services\Documents\django\html.venv\Lib\site-packages\django\db\models\query.py", line 1727, in order_by
    obj.query.add_ordering(*field_names)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Users\LabbeD\OneDrive - Facylities Multi Services\Documents\django\html.venv\Lib\site-packages\django\db\models\sql\query.py", line 2305, in add_ordering
    self.names_to_path(item.split(LOOKUP_SEP), self.model._meta)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\LabbeD\OneDrive - Facylities Multi Services\Documents\django\html.venv\Lib\site-packages\django\db\models\sql\query.py", line 1806, in names_to_path
    raise FieldError(
    ...<2 lines>...
    )
django.core.exceptions.FieldError: Cannot resolve keyword 'votes' into field. Choices are: choice, id, pub_date, question_text
>>> Question.objects.all().order_by("choice.votes")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\LabbeD\OneDrive - Facylities Multi Services\Documents\django\html.venv\Lib\site-packages\django\db\models\query.py", line 1727, in order_by
    obj.query.add_ordering(*field_names)
    ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Users\LabbeD\OneDrive - Facylities Multi Services\Documents\django\html.venv\Lib\site-packages\django\db\models\sql\query.py", line 2305, in add_ordering
    self.names_to_path(item.split(LOOKUP_SEP), self.model._meta)
    ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\LabbeD\OneDrive - Facylities Multi Services\Documents\django\html.venv\Lib\site-packages\django\db\models\sql\query.py", line 1806, in names_to_path
    raise FieldError(
    ...<2 lines>...
    )
django.core.exceptions.FieldError: Cannot resolve keyword 'choice.votes' into field. Choices are: choice, id, pub_date, question_text
>>> Question.objects.all().order_by("choice__votes")
<QuerySet [<Question: Quoi de neuf ?>, <Question: Quoi de neuf ?>, <Question: Quoi de neuf ?>, <Question: Django est-il une usine à gaz?>, <Question: Django est-il une usine à gaz?>, <Question: Django est-il une usine à gaz?>, <Question: Django a t'il du code legacy ?>, <Question: Django a t'il du code legacy ?>, <Question: Django a t'il du code legacy ?>, <Question: Django devrais t- il supprimer ses commandes?>, <Question: Django devrais t- il supprimer ses commandes?>, <Question: Django devrais t- il supprimer ses commandes?>, <Question: quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande?>, <Question: quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande?>, <Question: quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande?>, <Question: devrais-t-on supprimmer Django?>, <Question: devrais-t-on supprimmer Django?>, <Question: devrais-t-on supprimmer Django?>, <Question: Django est-il à l'image des politiciens ?>, <Question: Django est-il à l'image des politiciens ?>, '...(remaining elements truncated)...']>
>>> Question.objects.all().order_by("choice__votes").distinct()
<QuerySet [<Question: Quoi de neuf ?>, <Question: Django est-il une usine à gaz?>, <Question: Django a t'il du code legacy ?>, <Question: Django devrais t- il supprimer ses commandes?>, <Question: quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande?>, <Question: devrais-t-on supprimmer Django?>, <Question: Django est-il à l'image des politiciens ?>, <Question: Faudrait - il lister tout ce qui ne va pas chez Django?>]>

8


Question.objects.filter(contains(["question_text", "choice__choice_text"], "su"))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'contains' is not defined
>>> from django.db.models import Q
>>> Question.objects.filter(
...     Q(question_text__contains="ton_mot") | Q(choice__choice_text__contains="ton_mot")
... ).distinct()on_text__contains="ton_mot") | Q(choice__
  File "<console>", line 3
    ).distinct()on_text__contains="ton_mot") | Q(choice__
                                           ^
SyntaxError: unmatched ')'
>>> Question.objects.filter(Q(question_text__contains="su") | Q(choice__choice_text__contains="su")).distinct()
<QuerySet [<Question: Quoi de neuf ?>, <Question: Django devrais t- il supprimer ses commandes?>, <Question: quel est l'intérêt de faire des commandes pour Django pour coder en python alors que le reste de python ne fait pas de commande?>, <Question: devrais-t-on supprimmer Django?>]


12

listQuestionstr = [f"{user.id} {user.username} {user.first_name} {user.last_name} {user.email} {user.password} \n" for user in User.objects.all()]
>>> print("".join(listQuestionstr))
1 admin   admin@example.com pbkdf2_sha256$1000000$sj6urKlpBC5TdZ22Dd7Ca0$uyKs9nRZI8GNi1OhRNSJcVXb8+y3zAHtIb1Cg58PtV8=
2 ane    pbkdf2_sha256$1000000$kPwD1gEwhnPztfsbHx7ptR$u5a1yyWCDMObeGEGzw5fssoTX9lbxNV1N72BXjZIe6o=