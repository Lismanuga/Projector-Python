def cats_with_hats_optimized(num_cats, num_rounds):
    cats = [False] * num_cats  # Початково всі коти мають шапки
    for round in range(1, num_rounds + 1):
        for cat_number in range(round - 1, num_cats, round):
            cats[cat_number] = not cats[cat_number]  # Змінити стан кота
    cats_with_hats = [
        cat_number + 1 for cat_number, has_hat in enumerate(cats) if has_hat]
    return cats_with_hats


result = cats_with_hats_optimized(100, 100)
print("Cats with hats:", result)

# O(N*log(N))
