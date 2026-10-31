import sys, cv2, numpy as np
src, out, lo, hi = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
im = cv2.imread(src); h, w = im.shape[:2]
g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
g = cv2.bilateralFilter(g, 9, 60, 60)
e = cv2.Canny(g, lo, hi)
# küçük gürültüleri at: kısa kontürleri sil
n, lab, st, _ = cv2.connectedComponentsWithStats(e, 8)
keep = np.zeros_like(e)
for i in range(1, n):
    if st[i, cv2.CC_STAT_WIDTH] + st[i, cv2.CC_STAT_HEIGHT] >= 40: keep[lab == i] = 255
e = cv2.GaussianBlur(keep, (3, 3), 0)
bg = np.zeros((h, w, 3), np.float32); bg[:] = (20, 17, 15)  # BGR grafit
# pafta ızgarası
grid = np.zeros((h, w), np.float32)
for x in range(0, w, 60): grid[:, x] = 1
for y in range(0, h, 60): grid[y, :] = 1
ink = np.array((220, 228, 236), np.float32)  # açık kâğıt beyazı
bg += grid[..., None] * 0.06 * (ink - bg)
a = (e.astype(np.float32) / 255)[..., None] * 0.9
res = bg * (1 - a) + ink * a
cv2.imwrite(out, res.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 88])
