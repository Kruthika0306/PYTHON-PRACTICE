feedbacks = ["good", "bad", "good", "average", "good"]

good = feedbacks.count("good")
bad = feedbacks.count("bad")

print("Good feedbacks:", good)
print("Bad feedbacks:", bad)

if good > bad:
    print("Customer satisfaction is high ")
else:
    print("Needs improvement ")
