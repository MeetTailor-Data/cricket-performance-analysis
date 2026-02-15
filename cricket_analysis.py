import numpy as np

# Runs scored by players
p_score = np.array([
    [45, 60, 30, 80, 55],
    [70, 20, 90, 40, 65],
    [10, 35, 25, 50, 40],
    [95, 85, 70, 60, 75]
])

print("Player Scores:\n", p_score)

t_runs = np.sum(p_score, axis=1)
a_runs = np.mean(p_score, axis=1)

print("Total runs per player:", t_runs)
print("Average runs per player:", a_runs)

t_score = np.sum(p_score, axis=0)
m_score = np.max(p_score, axis=0)

print("Total runs per match:", t_score)
print("Highest score per match:", m_score)

print("Best player index:", np.argmax(t_runs))
print("Worst player index:", np.argmin(t_runs))


consistent_players = np.where(a_runs >= 50)[0]
print("Consistent players (avg >= 50):", consistent_players)


bonus = p_score + 10
final_score = np.clip(bonus, 0, 100)

print("Final scores after bonus:\n", final_score)
