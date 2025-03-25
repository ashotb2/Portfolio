num_of_steps = 3

report_template = """
Report

We have made {total_count} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads. The probabilities are {tails_fraction:.2f}% and {heads_fraction:.2f}%, respectively. Our forecast is that in the next {num_of_steps} observations we will have: {predicted_tails} tail and {predicted_heads} heads."""