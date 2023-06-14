from otree.api import *
import itertools
import math
from otree.models import player

doc = """
Your app description
"""


def creating_session(subsession):
    treatments = itertools.cycle([1, 2, 3, 4])
    for player in subsession.get_players():
        player.treatment = next(treatments)


class C(BaseConstants):
    NAME_IN_URL = 'infexp'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 30

    baseline_label1 = 'the rate of inflation will be 12% or higher'
    baseline_label2 = 'the rate of inflation will be between 8% and 12%'
    baseline_label3 = 'the rate of inflation will be between 4% and 8%'
    baseline_label4 = 'the rate of inflation will be between 2% and 4%'
    baseline_label5 = 'the rate of inflation will be between 0% and 2%'
    baseline_label6 = 'the rate of deflation (opposite of inflation) will be between 0% and 2%'
    baseline_label7 = 'the rate of deflation (opposite of inflation) will be between 2% and 4%'
    baseline_label8 = 'the rate of deflation (opposite of inflation) will be between 4% and 8%'
    baseline_label9 = 'the rate of deflation (opposite of inflation) will be between 8% and 12%'
    baseline_label10 = 'the rate of deflation (opposite of inflation) will be 12% or higher'

    income_label1 = 'Decrease'
    income_label2 = 'Stay about the same'
    income_label3 = 'Increase'

# adding labels for treatment four variable bins



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #für alle treatments
    treatment = models.IntegerField()

    #zählen für 2-step und endogenous method
    first_min_expectation = models.FloatField()
    first_max_expectation = models.FloatField()
    bisection_upper = models.BooleanField(label="", initial=False)
    bisection_lower = models.BooleanField(label="", initial=False)

    #2-step method
    min_expectation = models.FloatField(label="", blank=True)
    max_expectation = models.FloatField(label="", blank=True)
    min_expectation_q25 = models.FloatField()
    max_expectation_q25 = models.FloatField()
    min_expectation_q75 = models.FloatField()
    max_expectation_q75 = models.FloatField()
    midpoint = models.FloatField(label="")
    midpoint_final = models.FloatField(initial=0, blank=True)
    confirmation = models.BooleanField(label="")
    bisection = models.BooleanField(label="", blank=True)
    midpoint_q25 = models.FloatField(label="")
    midpoint_25_final = models.FloatField(initial=0, blank=True)
    midpoint_q75 = models.FloatField(label="")
    midpoint_75_final = models.FloatField(initial=0, blank=True)
    prolific = models.StringField(
        label="Please enter your Prolific ID:"
    )
    pointprog = models.FloatField(
        label="", blank=True,)

    # treatment: endogenous method
    min_expectation2 = models.FloatField(
        label="")
    first_min_expectation2 = models.FloatField()
    max_expectation2 = models.FloatField(
        label="")
    first_max_expectation2 = models.FloatField()
    midpoint2 = models.FloatField(initial=0)
    midpoint2_final = models.FloatField(initial=0, blank=True)
    min_expectation2_q25 = models.FloatField(initial=0)
    max_expectation2_q25 = models.FloatField(initial=0)
    bisection2 = models.BooleanField(label="", blank=True)
    range = models.FloatField(initial=0)
    midpoint2_q25 = models.FloatField(initial=0)
    midpoint2_25_final = models.FloatField(initial=0, blank=True)
    midpoint2_q75 = models.FloatField(initial=0)
    midpoint2_75_final = models.FloatField(initial=0, blank=True)
    range_q25 = models.FloatField(initial=0)
    range_q75 = models.FloatField(initial=0)
    round_number_q25 = models.FloatField(initial=0)
    min_expectation2_q75 = models.FloatField()
    max_expectation2_q75 = models.FloatField()
    number_of_rounds = models.FloatField(initial=1)
    number_of_rounds_q25 = models.FloatField(initial=1)
    number_of_rounds_q75 = models.FloatField(initial=1)
    rounded_num = models.IntegerField(initial=1)
    rounded_num_q25 = models.IntegerField(initial=1)
    rounded_num_q75 = models.IntegerField(initial=1)
    sum_q25 = models.IntegerField(initial=1)
    sum_q75 = models.IntegerField(initial=1)
    counting = models.IntegerField(initial=1)


    #treatment_bins
    q1_org_bin1 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin2 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin3 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin4 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin5 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin6 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin7 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin8 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin9 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin10 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin11 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q1_org_bin1_by_player = models.BooleanField(initial=False)
    q1_org_bin2_by_player = models.BooleanField(initial=False)
    q1_org_bin3_by_player = models.BooleanField(initial=False)
    q1_org_bin4_by_player = models.BooleanField(initial=False)
    q1_org_bin5_by_player = models.BooleanField(initial=False)
    q1_org_bin6_by_player = models.BooleanField(initial=False)
    q1_org_bin7_by_player = models.BooleanField(initial=False)
    q1_org_bin8_by_player = models.BooleanField(initial=False)
    q1_org_bin9_by_player = models.BooleanField(initial=False)
    q1_org_bin10_by_player = models.BooleanField(initial=False)
    q1_org_bin11_by_player = models.BooleanField(initial=False)
    q1_org_bin12_by_player = models.BooleanField(initial=False)
    q1_org_bin13_by_player = models.BooleanField(initial=False)
    q1_org_bin14_by_player = models.BooleanField(initial=False)
    # Sum of the bins answered by player
    q1_org_sum_by_player = models.IntegerField(initial=0)

    q1_org_sum = models.IntegerField(initial=0, blank=True)
    q1_org_sum_100 = models.BooleanField(initial=False, blank=True)
    q1_org_sum_0 = models.BooleanField(initial=False, blank=True)

    q3_org_sum = models.IntegerField(initial=0, blank=True)
    # Question 1: Fields for the sum of the bins (if estimates less/more than 100 in sum)
    q1_rep_sum = models.IntegerField(initial=0, blank=True)
    q1_rep_sum_100 = models.BooleanField(initial=False, blank=True)
    q1_rep_sum_0 = models.BooleanField(initial=False, blank=True)
    saw_q1_no_response_error = models.BooleanField(initial=False, required=False)
    answered_q1 = models.BooleanField(initial=False, required=False)

# adding all bin variables for treatment four

    q4_org_bin1 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin2 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin3 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin4 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin5 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin6 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin7 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin8 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin9 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin10 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin11 = models.IntegerField(min=0, max=100, blank=True, null=True, widget=widgets.TextInput())
    q4_org_bin1_by_player = models.BooleanField(initial=False)
    q4_org_bin2_by_player = models.BooleanField(initial=False)
    q4_org_bin3_by_player = models.BooleanField(initial=False)
    q4_org_bin4_by_player = models.BooleanField(initial=False)
    q4_org_bin5_by_player = models.BooleanField(initial=False)
    q4_org_bin6_by_player = models.BooleanField(initial=False)
    q4_org_bin7_by_player = models.BooleanField(initial=False)
    q4_org_bin8_by_player = models.BooleanField(initial=False)
    q4_org_bin9_by_player = models.BooleanField(initial=False)
    q4_org_bin10_by_player = models.BooleanField(initial=False)
    q4_org_bin11_by_player = models.BooleanField(initial=False)
    q4_org_bin12_by_player = models.BooleanField(initial=False)
    q4_org_bin13_by_player = models.BooleanField(initial=False)
    q4_org_bin14_by_player = models.BooleanField(initial=False)
    # Sum of the bins answered by player
    q4_org_sum_by_player = models.IntegerField(initial=0)

    q4_org_sum = models.IntegerField(initial=0, blank=True)
    q4_org_sum_100 = models.BooleanField(initial=False, blank=True)
    q4_org_sum_0 = models.BooleanField(initial=False, blank=True)

    q4_org_sum = models.IntegerField(initial=0, blank=True)
    # Question 4: Fields for the sum of the bins (if estimates less/more than 100 in sum)
    q4_rep_sum = models.IntegerField(initial=0, blank=True)
    q4_rep_sum_100 = models.BooleanField(initial=False, blank=True)
    q4_rep_sum_0 = models.BooleanField(initial=False, blank=True)
    saw_q4_no_response_error = models.BooleanField(initial=False, required=False)
    answered_q4 = models.BooleanField(initial=False, required=False)

    # demographic questions
    age = models.IntegerField(label="Age:")
    gender = models.IntegerField(label="Gender:", choices=[[-1, "Female"], [1, "Male"], [2, "Diverse"],
                                                           [3, "Prefer not to say"]],
                                 widget=widgets.RadioSelect)
    female = models.BooleanField(blank=True)
    income = models.IntegerField(
        label="",
        choices=[[1, "Less than £500"], [2, "£500 to £999"], [3, "£1,000 to £1,499"], [4, "£1,500 to £1,999"],
                 [5, "£2,000 to £2,499"], [6, "£2,500 to £2,999"], [7, "£2,000 to £2,499"], [8, "£3,000 to £3,499"],
                 [9, "£3,500 to £3,999"], [10, "£4,000 to £4,999"], [11, "£5,000 to £5,999"], [12, "£6,000 to £7,999"],
                 [13, "£8,000 to £9,999"], [14, "£10,000 or more"]])
    education = models.IntegerField(label="What is your highest level of educational attainment? ",
                                    choices=[[-1, "Prefer not to answer"], [1, "Less than high school diploma"],
                                             [2, "High school diploma"],
                                             [3, "Some college no degree"], [4, "Associate's degree occupational"],
                                             [5, "Associate's degree academic"], [6, "Bachelor's degree"],
                                             [7, "Master's degree"], [8, "Professional degree"],
                                             [9, "Doctoral degree"]],
                                    widget=widgets.RadioSelect)

    income1 = models.FloatField(label="", min=0, max=100, blank=True, intial=0)
    income2 = models.FloatField(label="", min=0, max=100, blank=True, intital=0)
    income3 = models.FloatField(label="", min=0, max=100, blank=True,)

    income1_by_player = models.BooleanField(initial=False)
    income2_by_player = models.BooleanField(initial=False)
    income3_by_player = models.BooleanField(initial=False)

    income_org_sum_by_player = models.IntegerField(initial=0)

    income_org_sum = models.IntegerField(initial=0, blank=True)
    income_org_sum_100 = models.BooleanField(initial=False, blank=True)
    income_org_sum_0 = models.BooleanField(initial=False, blank=True)

    # Question 1: Fields for the sum of the bins (if estimates less/more than 100 in sum)
    q3_rep_sum = models.IntegerField(initial=0, blank=True)
    q3_rep_sum_100 = models.BooleanField(initial=False, blank=True)
    q3_rep_sum_0 = models.BooleanField(initial=False, blank=True)
    saw_q3_no_response_error = models.BooleanField(initial=False, required=False)
    answered_q3 = models.BooleanField(initial=False, required=False)

    spending1 = models.FloatField(label="Major purchases (e.g. car, furniture, electrical appliances, etc.)")
    spending2 = models.FloatField(
        label="Essential goods (e.g. food and beverages, non-food items such as cleaning products or similar)")
    spending3 = models.FloatField(label="Clothing and footwear")
    spending4 = models.FloatField(label="Entertainment/recreation (e.g. restaurant visits, cultural events, gym)")
    spending5 = models.FloatField(
        label="Mobility (e.g. fuel, car loans and running costs, bus and train tickets)")
    spending6 = models.FloatField(
        label="Services (e.g. hairdresser, childcare, medical costs)")
    spending7 = models.FloatField(
        label="Travel, holidays")
    spending8 = models.FloatField(
        label="Housing costs (e.g. rent, mortgage, ancillary costs)")
    spending9 = models.FloatField(
        label="Financial reserves")

    major_purchases = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    essential_goods = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    clothing_and_footwear = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    entertainment_recreation = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    mobility = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    services = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    travel_holidays = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    housing_costs = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    financial_reserves = models.IntegerField(choices=[
        [1, 'Plan to spend more'],
        [2, 'Plan to spend roughly the same'],
        [3, 'Plan to spend less']
    ])

    question_dif = models.IntegerField(
        label="How easy or hard was it to answer the questions? Please select one answer.",
        choices=[[1, "Very difficult"], [2, "Somewhat difficult"], [3, "Partly interesting/partly uninteresting"],
                 [4, "Somewhat easy"], [5, "Very easy"]],
        widget=widgets.RadioSelect)
    question_length = models.IntegerField(
        label="How did you find the length of the survey?",
        choices=[[1, "Far too long"], [2, "Somewhat too Long"], [3, "Just right"],
                 [4, "Somewhat too short"], [5, "Far too short"]],
        widget=widgets.RadioSelect)

    survey_complete = models.BooleanField(Initial=False)

    bin4_label1 = models.StringField(),
    bin4_label2 = models.StringField(),
    bin4_label3 = models.StringField(),
    bin4_label4 = models.StringField(),
    bin4_label5 = models.StringField(),
    bin4_label6 = models.StringField(),
    bin4_label7 = models.StringField(),
    bin4_label8 = models.StringField(),
    bin4_label9 = models.StringField(),
    bin4_label10 = models.StringField(),


# FUNCTIONS

def midpoint(player: Player):
    # Funktion, die den midpoint ausrechnet und dabei je nach Antwort des Players entweder min oder max mit dem vorherigen midpoint ersetzt (bisection method)
    if player.round_number == 1:
        player.midpoint = (player.min_expectation + player.max_expectation) / 2
    else:
        if player.in_round(player.round_number - 1).bisection:
            player.max_expectation = player.in_round(player.round_number - 1).midpoint
            player.min_expectation = player.in_round(player.round_number - 1).min_expectation
            player.midpoint = (player.min_expectation + player.max_expectation) / 2
        else:
            player.min_expectation = player.in_round(player.round_number - 1).midpoint
            player.max_expectation = player.in_round(player.round_number - 1).max_expectation
            player.midpoint = (player.min_expectation + player.max_expectation) / 2
    return player.midpoint


def calculate_variables(pointprog):
    pointprogplus8 = pointprog + 8
    pointprogplus4 = pointprog + 4
    pointprogminus2 = pointprog - 2
    pointprogminus4 = pointprog - 4
    pointprogplus2 = pointprog + 2
    pointprogplus12 = pointprog + 12



    player.bin4_label1 = f'the rate of inflation will be {pointprogplus8}% or higher'
    player.bin4_label2 = f'the rate of inflation will be between {pointprogplus4}% and {pointprogplus8}%',
    player.bin4_label3 = f'the rate of inflation will be between {pointprog}% and {pointprogplus4}%',
    player.bin4_label4 = f'the rate of inflation will be between {pointprogminus2}% and {pointprog}%',
    player.bin4_label5 = f'the rate of inflation will be between {pointprogminus4}% and {pointprogminus2}%',
    player.bin4_label6 = f'the rate of deflation (opposite of inflation) will be between {pointprog}% and {pointprogplus2}%',
    player.bin4_label7 = f'the rate of deflation (opposite of inflation) will be between {pointprogplus2}% and {pointprogplus4}%',
    player.bin4_label8 = f'the rate of deflation (opposite of inflation) will be between {pointprogplus4}% and {pointprogplus8}%',
    player.bin4_label9 = f'the rate of deflation (opposite of inflation) will be between {pointprogplus8}% and {pointprogplus12}%',
    player.bin4_label10 = f'the rate of deflation (opposite of inflation) will be {pointprogplus12}% or higher'


def midpoint_q25(player: Player):
    if player.round_number == 2:
        player.midpoint_q25 = (player.in_round(1).min_expectation + player.midpoint_final) / 2
        player.max_expectation_q25 = player.midpoint_final
        player.min_expectation_q25 = player.in_round(2).min_expectation
    elif player.round_number > 2:
        if player.in_round(player.round_number - 1).bisection:
            player.max_expectation_q25 = player.in_round(player.round_number - 1).midpoint_q25
            player.min_expectation_q25 = player.in_round(player.round_number - 1).min_expectation_q25
            player.midpoint_q25 = (player.min_expectation_q25 + player.max_expectation_q25) / 2
        else:
            player.min_expectation_q25 = player.in_round(player.round_number - 1).midpoint_q25
            player.max_expectation_q25 = player.in_round(player.round_number - 1).max_expectation_q25
            player.midpoint_q25 = (player.min_expectation_q25 + player.max_expectation_q25) / 2
    return player.midpoint_q25



def midpoint_q75(player: Player):
    if player.round_number == 3:
        player.midpoint_q75 = (player.in_round(1).max_expectation + player.in_round(2).midpoint_final) / 2
        player.max_expectation_q75 = player.in_round(1).max_expectation
        player.min_expectation_q75 = player.in_round(2).midpoint_final
    elif player.round_number > 3:
        if player.in_round(player.round_number - 1).bisection:
            player.max_expectation_q75 = player.in_round(player.round_number - 1).midpoint_q75
            player.min_expectation_q75 = player.in_round(player.round_number - 1).min_expectation_q75
            player.midpoint_q75 = (player.min_expectation_q75 + player.max_expectation_q75) / 2
        else:
            player.min_expectation_q75 = player.in_round(player.round_number - 1).midpoint_q75
            player.max_expectation_q75 = player.in_round(player.round_number - 1).max_expectation_q75
            player.midpoint_q75 = (player.min_expectation_q75 + player.max_expectation_q75) / 2
    return player.midpoint_q75


#endogenous method

def midpoint2(player: Player):
    # Funktion, die den midpoint ausrechnet und dabei je nach Antwort des Players entweder min oder max mit dem vorherigen midpoint ersetzt (bisection method)
    if player.round_number == 1:
        player.midpoint2 = (player.min_expectation2 + player.max_expectation2) / 2
    else:
        if player.in_round(player.round_number - 1).bisection2:
            player.max_expectation2 = player.in_round(player.round_number - 1).midpoint2
            player.min_expectation2 = player.in_round(player.round_number - 1).min_expectation2
            player.midpoint2 = (player.min_expectation2 + player.max_expectation2) / 2
        else:
            player.min_expectation2 = player.in_round(player.round_number - 1).midpoint2
            player.max_expectation2 = player.in_round(player.round_number - 1).max_expectation2
            player.midpoint2 = (player.min_expectation2 + player.max_expectation2) / 2
    return player.midpoint2






def rangey(player: Player):
    player.range = player.in_round(1).first_max_expectation - player.in_round(1).first_min_expectation
    return player.range


def midpoint_q25_endo(player: Player):
    if player.round_number == round_number_endo(player):
        player.midpoint2_q25 = (player.in_round(1).first_min_expectation + player.midpoint2_final) / 2
        player.max_expectation2_q25 = player.in_round(round_number_endo(player)).midpoint2_final
        player.min_expectation2_q25 = player.in_round(1).first_min_expectation
    else:
        if player.in_round(player.round_number - 1).bisection2:
            player.max_expectation2_q25 = player.in_round(player.round_number - 1).midpoint2_q25
            player.min_expectation2_q25 = player.in_round(player.round_number - 1).min_expectation2_q25
            player.midpoint2_q25 = (player.min_expectation2_q25 + player.max_expectation2_q25) / 2
        else:
            player.min_expectation2_q25 = player.in_round(player.round_number - 1).midpoint2_q25
            player.max_expectation2_q25 = player.in_round(player.round_number - 1).max_expectation2_q25
            player.midpoint2_q25 = (player.min_expectation2_q25 + player.max_expectation2_q25) / 2
    return player.midpoint2_q25


def midpoint_q75_endo(player: Player):
    if player.round_number == sum_q25(player):
        player.midpoint2_q75 = (player.in_round(1).first_max_expectation + player.in_round(round_number_endo(player)).midpoint2_final) / 2
        player.min_expectation2_q75 = player.in_round(round_number_endo(player)).midpoint2_final
        player.max_expectation2_q75 = player.in_round(1).first_max_expectation
    elif player.round_number > sum_q25(player):
        if player.in_round(player.round_number - 1).bisection2:
            player.max_expectation2_q75 = player.in_round(player.round_number - 1).midpoint2_q75
            player.min_expectation2_q75 = player.in_round(player.round_number - 1).min_expectation2_q75
            player.midpoint2_q75 = (player.min_expectation2_q75 + player.max_expectation2_q75) / 2
        else:
            player.min_expectation2_q75 = player.in_round(player.round_number - 1).midpoint2_q75
            player.max_expectation2_q75 = player.in_round(player.round_number - 1).max_expectation2_q75
            player.midpoint2_q75 = (player.min_expectation2_q75 + player.max_expectation2_q75) / 2
    return player.midpoint2_q75


def range_q25(player: Player):
    if rangey(player) > 1: #and player.round_number == round_number_endo(player):
        player.range_q25 = player.in_round(round_number_endo(player)).midpoint2_final - player.in_round(1).first_min_expectation
    return player.range_q25


def range_q75(player: Player):
    if rangey(player) > 1:
        player.range_q75 = player.in_round(1).first_max_expectation - player.in_round(round_number_endo(player)).midpoint2_final
    return player.range_q75


def round_number_endo(player: Player):
    player.number_of_rounds = math.log(player.in_round(1).range, 2)
    if rangey(player) > 1 and player.number_of_rounds < 1:
        player.rounded_num = 1
    else:
        player.rounded_num = math.floor(player.number_of_rounds)
    return player.rounded_num

def round_number_endo_q25(player: Player):
    if range_q25(player) <= 1:
        player.rounded_num_q25 = 0
    else:
        player.number_of_rounds_q25 = math.log(range_q25(player), 2)
        if range_q25(player) > 1 and player.number_of_rounds_q25 < 1:
            player.rounded_num_q25 = 1
        else:
            player.rounded_num_q25 = math.floor(player.number_of_rounds_q25)
    return player.rounded_num_q25

def round_number_endo_q75(player: Player):
    if range_q75(player) <= 1:
        player.rounded_num_q75 = 0
    else:
        player.number_of_rounds_q75 = math.log(range_q75(player), 2)
        if range_q75(player) > 1 and player.number_of_rounds_q75 < 1:
            player.rounded_num_q75 = 1
        else:
            player.rounded_num_q75 = math.floor(player.number_of_rounds_q75)
    return player.rounded_num_q75

def sum_q25(player: Player):
    if round_number_endo_q25(player) == 0:
        player.sum_q25 = round_number_endo(player)
    else:
        player.sum_q25 = round_number_endo(player) + round_number_endo_q25(player) - 1
    return player.sum_q25

def sum_q75(player: Player):
    if range_q75(player) > 1:
        player.sum_q75 = sum_q25(player) + round_number_endo_q75(player) - 1
    else:
        player.sum_q75 = sum_q25(player)
    return player.sum_q75



def sum_bins(b_list):
        total = 0
        for b in b_list:
            total += b
        return total



def sum_incomes(i_list):
        total_i = 0
        for i in i_list:
            total_i += i
        return total_i

# PAGES
class Instructions(Page):
    form_model = "player"
    form_fields = ["prolific"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Point(Page):
    form_model = "player"
    form_fields = ["pointprog"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class InflationsErwartung(Page):
    # Spieler werden in Runde 1 nach Inflationserwartung gefragt
    form_model = "player"
    form_fields = ["min_expectation", "max_expectation"]

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 1 and player.round_number == 1

    @staticmethod
    def error_message(player: Player, values):
        if values['min_expectation'] == None:
            return "Please enter your inflation expectation."
        elif values['max_expectation'] == None:
            return "Please enter your inflation expectation."
        elif values['min_expectation'] > values['max_expectation']:
            return 'Your Minimum Inflation Expectation cannot be larger than your Maximum Inflation Expectation.'
        elif values['min_expectation'] == values['max_expectation']:
            return 'Minimum und maximum inflation expectation cannot be the same.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.first_min_expectation = player.min_expectation
        player.first_max_expectation = player.max_expectation
        return player.first_min_expectation and player.first_max_expectation




class InflationsErwartung3(Page):
    # Spieler werden in Runde 1 nach Inflationserwartung gefragt
    form_model = "player"
    form_fields = ["min_expectation", "max_expectation"]

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 1 and player.round_number == 1 and player.confirmation == False

    @staticmethod
    def error_message(player: Player, values):
        if values['min_expectation'] == None:
            return "Please enter your inflation expectation."
        elif values['max_expectation'] == None:
            return "Please enter your inflation expectation."
        elif values['min_expectation'] > values['max_expectation']:
            return 'Your Minimum Inflation Expectation cannot be larger than your Maximum Inflation Expectation'
        elif values['min_expectation'] == values['max_expectation']:
            return 'Minimum und maximum inflation expectation cannot be the same.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.first_min_expectation = player.min_expectation
        player.first_max_expectation = player.max_expectation
        return player.first_min_expectation and player.first_max_expectation



class Confirmation(Page):
    form_model = 'player'
    form_fields = ['confirmation']

    def is_displayed(player: Player):
        return player.round_number == 1 and player.treatment == 1

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            min_expectation=player.in_round(1).min_expectation,
            max_expectation=player.in_round(1).max_expectation,
            mid_point=midpoint(player)
        )

class InstructionsP2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 1 and player.round_number == 1 or player.treatment == 3 and player.round_number == 1 and rangey(player) > 1


class Bisection(Page):
    form_model = "player"
    form_fields = ["bisection"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number >= 1 and player.round_number <= 2 and player.treatment == 1

    @staticmethod
    def error_message(player: Player, values):
        if values['bisection']==None:
            return "Please choose an option."

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
                min_expectation=player.in_round(1).first_min_expectation,
                max_expectation=player.in_round(1).first_max_expectation,
                mid_point=round(midpoint(player), 2),
                roundnumber=player.round_number
        )


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.bisection == True:
            player.bisection_lower = True
            player.bisection_upper = False
        else:
            player.bisection_upper = True
            player.bisection_lower = False
        if player.round_number == 2:
            if player.bisection:
                player.max_expectation = player.midpoint
                player.midpoint_final = (player.min_expectation + player.max_expectation) / 2
            else:
                player.min_expectation = player.midpoint
                player.midpoint_final = (player.min_expectation + player.max_expectation) / 2
        return player.midpoint_final and player.bisection_upper and player.bisection_lower




class Q25(Page):
    form_model = "player"
    form_fields = ["bisection"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number >= 2 and player.round_number <= 3 and player.treatment == 1

    @staticmethod
    def error_message(player: Player, values):
        if values['bisection']==None:
            return "Please choose an option."

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 2:
            return dict(
                min_expectation=player.in_round(1).first_min_expectation,
                mid_point=round(player.in_round(2).midpoint_final, 2),
                midpoint_q25=round(midpoint_q25(player), 2),
                roundnumber=1
            )
        else:
            return dict(
                min_expectation=player.in_round(1).first_min_expectation,
                mid_point=round(player.in_round(2).midpoint_final, 2),
                midpoint_q25=round(midpoint_q25(player), 2),
                roundnumber=2
            )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.bisection == True:
            player.bisection_lower = True
            player.bisection_upper = False
        else:
            player.bisection_upper = True
            player.bisection_lower = False
        if player.round_number == 3:
            if player.bisection:
                player.max_expectation_q25 = player.midpoint_q25
                player.midpoint_25_final = (player.min_expectation_q25 + player.max_expectation_q25) / 2
            else:
                player.min_expectation_q25 = player.midpoint_q25
                player.midpoint_25_final = (player.min_expectation_q25 + player.max_expectation_q25) / 2
        return player.midpoint_25_final and player.bisection_lower and player.bisection_upper




class Q75(Page):
    form_model = "player"
    form_fields = ["bisection"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number >= 3 and player.round_number <= 4 and player.treatment == 1

    @staticmethod
    def error_message(player: Player, values):
        if values['bisection']==None:
            return "Please choose an option."

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 3:
            return dict(
                max_expectation=player.in_round(1).first_max_expectation,
                mid_point=round(player.in_round(2).midpoint_final, 2),
                midpoint_q75=round(midpoint_q75(player), 2),
                roundnumber=1
            )
        else:
            return dict(
                max_expectation=player.in_round(1).first_max_expectation,
                mid_point=round(player.in_round(2).midpoint_final, 2),
                midpoint_q75=round(midpoint_q75(player), 2),
                roundnumber=2
            )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.bisection == True:
            player.bisection_lower = True
            player.bisection_upper = False
        else:
            player.bisection_upper = True
            player.bisection_lower = False
        if player.round_number == 4:
            if player.bisection:
                player.max_expectation_q75 = player.midpoint_q75
                player.midpoint_75_final = (player.min_expectation_q75 + player.max_expectation_q75) / 2
            else:
                player.min_expectation_q75 = player.midpoint_q75
                player.midpoint_75_final = (player.min_expectation_q75 + player.max_expectation_q75) / 2
        return player.midpoint_75_final and player.bisection_lower and player.bisection_upper



class Q25Screen(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 2  and player.treatment == 1

    def vars_for_template(player: Player):
            return dict(
                roundnumber=player.round_number
            )


class Q75Screen(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 3 and player.treatment == 1

    def vars_for_template(player: Player):
        return dict(
            roundnumber=player.round_number
        )


# Pages treatment endo
class InflationsErwartung2(Page):
    # Spieler werden in Runde 1 nach Inflationserwartung gefragt
    form_model = "player"
    form_fields = ["min_expectation2", "max_expectation2"]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.treatment == 3

    @staticmethod
    def error_message(player: Player, values):
        if values['min_expectation2'] == None:
            return "Please enter your inflation expectation."
        elif values['max_expectation2'] == None:
            return "Please enter your inflation expectation."
        elif values['min_expectation2'] > values['max_expectation2']:
            return 'Your Minimum Inflation Expectation cannot be larger than your Maximum Inflation Expectation'
        elif values['min_expectation2'] == values['max_expectation2']:
            return 'Minimum und maximum inflation expectation cannot be the same.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.first_min_expectation = player.min_expectation2
        player.first_max_expectation = player.max_expectation2
        if rangey(player) <= 1:
            return player.midpoint2 and player.first_min_expectation and player.first_max_expectation
        else:
            return player.first_min_expectation and player.first_max_expectation and rangey(player)



class InflationsErwartung4(Page):
    # Spieler werden in Runde 1 nach Inflationserwartung gefragt
    form_model = "player"
    form_fields = ["min_expectation2", "max_expectation2"]

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 3 and player.round_number == 1 and player.confirmation == False

    @staticmethod
    def error_message(player: Player, values):
        if values['min_expectation2'] == None:
            return "Please enter your inflation expectation."
        elif values['max_expectation2'] == None:
            return "Please enter your inflation expectation."
        elif values['min_expectation2'] > values['max_expectation2']:
            return 'Your Minimum Inflation Expectation cannot be larger than your Maximum Inflation Expectation'
        elif values['min_expectation2'] == values['max_expectation2']:
            return 'Minimum und maximum inflation expectation cannot be the same.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.first_min_expectation = player.min_expectation2
        player.first_max_expectation = player.max_expectation2
        if rangey(player) <= 1:
            player.midpoint2_final = midpoint2(player)
            return player.midpoint2_final and player.first_min_expectation and player.first_max_expectation
        else:
            return player.first_min_expectation and player.first_max_expectation and rangey(player)


class ConfirmationEndo(Page):
    form_model = 'player'
    form_fields = ['confirmation']

    def is_displayed(player: Player):
        return player.round_number == 1 and player.treatment == 3

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            min_expectation=player.in_round(1).min_expectation2,
            max_expectation=player.in_round(1).max_expectation2,
            mid_point=midpoint2(player)
        )


class Bisection2(Page):
    form_model = "player"
    form_fields = ["bisection2"]

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 3 and player.round_number <= round_number_endo(player) and rangey(player) > 1

    @staticmethod
    def error_message(player: Player, values):
        if values['bisection2']==None:
            return "Please choose an option."


    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == 1:
            return dict(
                min_expectation2 = player.in_round(1).first_min_expectation,
                max_expectation2 = player.in_round(1).first_max_expectation,
                mid_point2=round(midpoint2(player), 2),
                range = rangey(player),
                number_of_rounds = round_number_endo(player),
                counting = player.counting
                    )
        else:

            return dict(
                min_expectation2 = player.in_round(1).first_min_expectation,
                max_expectation2 = player.in_round(1).first_max_expectation,
                mid_point2=round(midpoint2(player), 2),
                range = rangey(player),
                number_of_rounds = round_number_endo(player),
                counting = player.in_round(player.round_number - 1).counting,
                number_of_rounds_q25 = round_number_endo_q25(player)
            )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.bisection2 == True:
            player.bisection_lower = True
            player.bisection_upper = False
        else:
            player.bisection_upper = True
            player.bisection_lower = False
        if player.round_number == 1:
            player.counting += 1
        elif player.round_number == round_number_endo(player):
            player.counting = 1
        else:
            player.counting = player.in_round(player.round_number - 1).counting + 1

        if player.round_number == round_number_endo(player):
            if player.bisection2:
                player.max_expectation2 = player.midpoint2
                player.midpoint2_final = (player.min_expectation2 + player.max_expectation2) / 2
            else:
                player.min_expectation2 = player.midpoint2
                player.midpoint2_final = (player.min_expectation2 + player.max_expectation2) / 2
        return player.midpoint2_final and player.counting and player.bisection_upper and player.bisection_lower and player.range_q75 and player.range_q25


class Q25EndoScreen(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 3 and player.round_number == round_number_endo(player) and round_number_endo_q25(player) != 0


class Q25Endo(Page):
    form_model = 'player'
    form_fields = ['bisection2']

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 3 and player.round_number >= round_number_endo(player) and player.round_number <= sum_q25(player) and range_q25(player) > 1

    @staticmethod
    def error_message(player: Player, values):
        if values['bisection2']==None:
            return "Please choose an option."

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == round_number_endo(player):
            return dict(

                min_expectation2 = player.in_round(1).first_min_expectation,
                mid_point2 = round(player.midpoint2_final, 2),
                midpoint2_q25=round(midpoint_q25_endo(player),2),
                max_expectation3 = player.max_expectation2_q25,
                number_of_rounds_q = round_number_endo_q25(player),
                counting = 1
                )
        else:
            return dict(
                min_expectation2 = player.in_round(1).first_min_expectation,
                mid_point2 = round(player.in_round(round_number_endo(player)).midpoint2_final, 2),
                midpoint2_q25=round(midpoint_q25_endo(player),2),
                max_expectation3 = player.max_expectation2_q25,
                number_of_rounds_q = round_number_endo_q25(player),
                counting = player.in_round(player.round_number - 1).counting
                )



    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.bisection2 == True:
            player.bisection_lower = True
            player.bisection_upper = False
        else:
            player.bisection_upper = True
            player.bisection_lower = False
        if player.round_number == sum_q25(player):
            player.counting = 1
        elif player.round_number == round_number_endo(player):
            player.counting += 1
        else:
            player.counting = player.in_round(player.round_number-1).counting+1

        if player.round_number >= round_number_endo(player) and player.round_number == round_number_endo_q25(player):
            if player.bisection2:
                player.max_expectation2_q25 = player.midpoint2_q25
                player.midpoint2_25_final = (player.min_expectation2_q25 + player.max_expectation2_q25) / 2
            else:
                player.min_expectation2_q25 = player.midpoint2_q25
                player.midpoint2_25_final = (player.min_expectation2_q25 + player.max_expectation2_q25) / 2
        return player.midpoint2_25_final and player.bisection_upper and player.bisection_lower and player.counting



class Q75EndoScreen(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 3 and player.round_number >= round_number_endo(player) and player.round_number == sum_q25(player) and range_q75(player) > 1

    @staticmethod
    def vars_for_template(player: Player):
            return dict(
                max_expectation2 = player.in_round(1).first_max_expectation,
                mid_point2 = round(player.in_round(round_number_endo(player)).midpoint2_final, 2),
                midpoint2_q75=round(midpoint_q75_endo(player), 2),
                max_expectation4 = player.max_expectation2_q75,
                number_of_rounds=round_number_endo(player),
                min_expectation4 = player.min_expectation2_q75,
                sum_q25 = sum_q25(player),
                sum_q75 = sum_q75(player),
                counting = 1,
                range_q75 = range_q75(player)
                )


class Q75Endo(Page):
    form_model = 'player'
    form_fields = ['bisection2']

    @staticmethod
    def error_message(player: Player, values):
        if values['bisection2']==None:
            return "Please choose an option."

    @staticmethod
    def vars_for_template(player: Player):
        if player.round_number == sum_q25(player):
            return dict(
                max_expectation2 = player.in_round(1).first_max_expectation,
                mid_point2 = round(player.in_round(round_number_endo(player)).midpoint2_final, 2),
                midpoint2_q75=round(midpoint_q75_endo(player), 2),
                max_expectation4 = player.max_expectation2_q75,
                number_of_rounds_q=round_number_endo_q75(player),
                min_expectation4 = player.min_expectation2_q75,
                sum_q25 = sum_q25(player),
                sum_q75 = sum_q75(player),
                counting = 1
                )
        else:
            return dict(
                max_expectation2 = player.in_round(1).first_max_expectation,
                mid_point2 = round(player.in_round(round_number_endo(player)).midpoint2_final, 2),
                midpoint2_q75=round(midpoint_q75_endo(player), 2),
                max_expectation4 = player.max_expectation2_q75,
                min_expectation4 = player.min_expectation2_q75,
                number_of_rounds_q=round_number_endo_q75(player),
                sum_q25 = sum_q25(player),
                sum_q75 = sum_q75(player),
                counting = player.in_round(player.round_number - 1).counting
            )

    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 3 and player.round_number >= round_number_endo(player) and player.round_number >= sum_q25(player) and player.round_number <= sum_q75(player) and range_q75(player) > 1


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.bisection2 == True:
            player.bisection_lower = True
            player.bisection_upper = False
        else:
            player.bisection_upper = True
            player.bisection_lower = False
        if player.round_number == sum_q25(player):
            player.counting += 1
        else:
            player.counting = player.in_round(player.round_number - 1).counting + 1


        if player.round_number == round_number_endo_q75(player):
            if player.bisection2:
                player.max_expectation2_q75 = player.midpoint2_q75
                player.midpoint2_75_final = (player.min_expectation2_q75 + player.max_expectation2_q75) / 2
            else:
                player.min_expectation2_q75 = player.midpoint2_q75
                player.midpoint2_75_final = (player.min_expectation2_q75 + player.max_expectation2_q75) / 2
        return player.midpoint2_75_final and player.counting and player.bisection_upper and player.bisection_lower

# treatment bins

class Bins(Page):
    form_model = "player"
    @staticmethod
    def is_displayed(player: Player):
        return player.treatment == 2 and player.round_number == 1

    @staticmethod
    def error_message(player: Player, values):
        if player.treatment == 2:
            fields = [f'q1_org_bin{i}' for i in range(1, 12)]
            totals = 0
            for field in fields:
                value = values.get(field, 0)
                if not value:
                    value = 0
                totals += int(value)

            if totals != 100:
                return 'Please make sure the values add to 100'


    @staticmethod
    def get_form_fields(player):
        if player.treatment == 2:
            return [f'q1_org_bin{i}' for i in range(1, 11)]

    @staticmethod
    def vars_for_template(player: Player):
        if player.treatment == 2:
            fields = [f'q1_org_bin{i}' for i in range(1, 11)]
            labels = [getattr(C, f'baseline_label{i}') for i in range(1, 11)]
        combined = zip(labels, fields)
        return dict(combined=combined)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.saw_q1_no_response_error = True
        # First try if the bins are empty. If yes, replace with 0
        for i in range(1, 11):
            try:
                getattr(player, 'q1_org_bin' + str(i))
                exec("{0} = {1}".format('player.q1_org_bin' + str(i) + '_by_player', True))
            except TypeError:
                exec("{0} = {1}".format('player.q1_org_bin' + str(i), 0))
                # {0} and {1} are indices to be replaced by the arguments of .format

        bins = [getattr(player, f'q1_org_bin{i}') for i in range(1, 11)]
        player.q1_org_sum = sum_bins(bins)
        bins_by_player = [getattr(player, f'q1_org_bin{i}_by_player') for i in range(1, 11)]
        player.q1_org_sum_by_player = sum_bins(bins_by_player)

        # Case 1: Beliefs add up to 100
        if player.q1_org_sum == 100:
            player.q1_org_sum_100 = True
            player.answered_q1 = True

        # Case 2: Beliefs add up to 0 (i.e. participant didn't enter anything)
        # In this case set them to none again to restart the density question
        if player.q1_org_sum == 0:
            player.q1_org_sum_0 = True
            for i in range(1, 11):
                exec("{0} = {1}".format('player.q1_org_bin' + str(i), None))

        if timeout_happened:
            player.has_timeout = True
            player.session.dropout_treatments.append(player.treatment)



# demographics


class bins4(Page):
        form_model = "player"

        @staticmethod
        def vars_for_template(player: Player):
            return dict(
                pointprog=player.pointprog,
            )


        @staticmethod
        def error_message(player: Player, values):
            if player.treatment == 4:
                fields = [f'q4_org_bin{i}' for i in range(1, 12)]
                totals = 0
                for field in fields:
                    value = values.get(field, 0)
                    if not value:
                        value = 0
                    totals += int(value)

                if totals != 100:
                    return 'Please make sure the values add to 100'

        @staticmethod
        def get_form_fields(player):
            if player.treatment == 4:
                return [f'q4_org_bin{i}' for i in range(1, 11)]

        @staticmethod
        def vars_for_template(player: Player):
            if player.treatment == 4:
                fields = [f'q4_org_bin{i}' for i in range(1, 11)]
                labels = [getattr(Player(),f'bin4_label{i}') for i in range(1, 11)]
            combined = zip(labels, fields)
            return dict(combined=combined)


        @staticmethod
        def before_next_page(player, timeout_happened):
            player.saw_q4_no_response_error = True
            # First try if the bins are empty. If yes, replace with 0
            for i in range(1, 11):
                try:
                    getattr(player, 'q4_bin' + str(i))
                    exec("{0} = {1}".format('player.q4_bin' + str(i) + '_by_player', True))
                except TypeError:
                    exec("{0} = {1}".format('player.q4_bin' + str(i), 0))
                    # {0} and {1} are indices to be replaced by the arguments of .format

            bins = [getattr(player, f'q4_bin{i}') for i in range(1, 11)]
            player.q4_sum = sum_bins(bins)
            bins_by_player = [getattr(player, f'q4_bin{i}_by_player') for i in range(1, 11)]
            player.q4_sum_by_player = sum_bins(bins_by_player)

            # Case 1: Beliefs add up to 100
            if player.q4_sum == 100:
                player.q4_sum_100 = True
                player.answered_q4 = True

            # Case 2: Beliefs add up to 0 (i.e. participant didn't enter anything)
            # In this case set them to none again to restart the density question
            if player.q4_sum == 0:
                player.q4_sum_0 = True
                for i in range(1, 11):
                    exec("{0} = {1}".format('player.q4_bin' + str(i), None))

            if timeout_happened:
                player.has_timeout = True
                player.session.dropout_treatments.append(player.treatment)


class Demo1(Page):
    form_model = "player"
    form_fields = ["gender", "age"]

    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False

    # def vars_for_template(player: Player):
    #     if player.round_number == sum_q25(player):
    #         return dict(
    #             player.round_number =
    #         )

class Demo2(Page):
    form_model = "player"
    form_fields = ["income", "education"]

    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False

class Demo3(Page):
    form_model = "player"

    @staticmethod
    def error_message(player: Player, values):
        if player.treatment in [1, 2, 3]:
            fields = [f'income{i}' for i in range(1, 4)]
            total_i = 0
            for field in fields:
                value_income = values.get(field)
                if not value_income:
                    value_income = 0
                total_i += int(value_income)
            if total_i != 100:
                return 'Please make sure the values add up to 100.'

    @staticmethod
    def get_form_fields(player):
            return [f'income{i}' for i in range(1, 4)]

    @staticmethod
    def vars_for_template(player: Player):
        if player.treatment == 1 or player.treatment == 2 or player.treatment == 3:
            fields = [f'income{i}' for i in range(1, 4)]
            labels = [getattr(C, f'income_label{i}') for i in range(1, 4)]
        combined = zip(labels, fields)
        return dict(combined=combined)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.saw_q3_no_response_error = True
        # First try if the bins are empty. If yes, replace with 0
        for i in range(1, 4):
            try:
                getattr(player, 'income' + str(i))
                exec("{0} = {1}".format('player.income' + str(i) + '_by_player', True))
            except TypeError:
                exec("{0} = {1}".format('player.income' + str(i), 0))
                # {0} and {1} are indices to be replaced by the arguments of .format

        incomes = [getattr(player, f'income{i}') for i in range(1, 4)]




    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False


class Demo4(Page):
    form_model = "player"
    form_fields = ["spending1", "spending2", "spending3", "spending4", "spending5", "spending6", "spending7",
                   "spending8", "spending9"]

    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False


class Demo5(Page):
    form_model = "player"
    form_fields = ["major_purchases", "essential_goods", "clothing_and_footwear", "entertainment_recreation",
                   "mobility", "services", "travel_holidays", "housing_costs", "financial_reserves"]

    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if not timeout_happened and player.treatment == [1, 2, 3]:
            player.survey_complete = True
        else:
            player.survey_complete = False

class Demo6(Page):
    form_model = "player"
    form_fields = ["question_dif", "question_length"]

    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False




class Final(Page):
    form_model = "player"

    @staticmethod
    def js_vars(player):
        return dict(
            completionlink=
            player.subsession.session.config['completionlink']
        )

    pass
    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False


class Code(Page):
    form_model = "player"


    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False



class DemoIntro(Page):

    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False



class FinanceIntro(Page):

    @staticmethod
    def is_displayed(player: Player):
        if player.treatment == 1 and player.round_number == 5:
            return True
        elif player.treatment == 2 and player.round_number == 1:
            return True
        elif player.treatment == 3 and (player.round_number == sum_q75(player) or player.in_round(1).range <= 1):
            return True
        else:
            return False



page_sequence = [Instructions, Point, InflationsErwartung, Confirmation, InflationsErwartung3, InflationsErwartung2, ConfirmationEndo, InflationsErwartung4, InstructionsP2, Bisection, Bins, bins4, Q25Screen,Q25, Q75Screen, Q75,
                 Bisection2, Q25EndoScreen, Q25Endo, Q75EndoScreen,
                 Q75Endo, Demo6, DemoIntro, Demo1, FinanceIntro, Demo2, Demo3, Demo4, Demo5, Final, Code]