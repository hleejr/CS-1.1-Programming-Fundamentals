import person

def test_person_init():
    """confirm init complete"""
    my_person = person.Person(3,False)
    assert my_person._id is 3
    assert my_person.infected is False

def test_person_survival():
    # tests the did survive infection function
    my_person = person.Person(0,False,True)
    my_person.did_survive_infection(0) #Cant kill you
    assert my_person.is_alive is True
    my_person.did_survive_infection(1) #Has to kill you
    assert my_person.is_alive is False
