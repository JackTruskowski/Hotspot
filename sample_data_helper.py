from website.models import Sample

s = Sample(restaurant_name="Burrito Drive", rating=3.5)
s.save()

s = Sample(restaurant_name="McDonalds", rating=1.2)
s.save()

s = Sample(restaurant_name="Badger Market", rating=2.0)
s.save()
