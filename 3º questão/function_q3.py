selRoi = 1
initial = 0
top_left= [160,213]
bottom_right = [320,426]
first_time = 1

def normalizeImage(v):
  v = (v - v.min()) / (v.max() - v.min())
  result = (v * 255).astype(np.uint8)
  return result
