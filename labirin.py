import tkinter as tk
from collections import deque

# ============================================================
# LABIRIN - mirip foto tugas, 27x27 grid, TERHUBUNG S ke E
# '#' = dinding, ' ' = jalan, 'S' = start (.), 'E' = exit
# ============================================================
MAZE = [
    "###########################",   # 0
    "#S    #   #       #       #",   # 1
    "# ### # # # ##### # ##### #",   # 2
    "# #   # # #     # #     # #",   # 3
    "# # ### # ##### # ##### # #",   # 4
    "# #     #     # #   #   # #",   # 5
    "# ####### ### # ### # ### #",   # 6
    "#         # # #   # # #   #",   # 7
    "######### # # ### # # # ###",   # 8
    "#       # # #   # # # #   #",   # 9
    "# ##### # # ### # # # ### #",   # 10
    "# #   # # #   # # #     # #",   # 11
    "# # # # # # # # # ####### #",   # 12
    "# # # # # # # # #         #",   # 13
    "# # # ### # # # ###########",   # 14
    "# # #     # # #           #",   # 15
    "# # ####### # ########### #",   # 16
    "# #         #     #       #",   # 17
    "# ########### ### # ##### #",   # 18
    "#           # # # #     # #",   # 19
    "########### # # # ##### # #",   # 20
    "#         # # # #     # # #",   # 21
    "# ####### # # # ##### # # #",   # 22
    "# #     # # # #     # # # #",   # 23
    "# # ### # # # ##### # # # #",   # 24
    "# #   #             #    E#",   # 25
    "###########################",   # 26
]

ROWS = len(MAZE)
COLS = len(MAZE[0])

# Temukan posisi Start dan End
START = END = None
for r, row in enumerate(MAZE):
    for c, ch in enumerate(row):
        if ch == 'S': START = (r, c)
        elif ch == 'E': END = (r, c)

# ============================================================
# BFS - mencari jalur terpendek
# ============================================================
def bfs(maze, start, end):
    queue = deque([(start, [start])])
    visited = {start}
    explored_order = []

    while queue:
        (r, c), path = queue.popleft()
        explored_order.append((r, c))

        if (r, c) == end:
            return path, explored_order

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if maze[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return None, explored_order


# ============================================================
# GUI - Tkinter
# ============================================================
CELL = 22       # ukuran pixel per sel
PAD  = 10       # padding canvas

COLOR_WALL    = "#1a2744"
COLOR_PATH    = "#ffffff"
COLOR_START   = "#1abc9c"
COLOR_END     = "#f39c12"
COLOR_VISITED = "#a8dbc9"   # sel BFS dieksplorasi (hijau muda)
COLOR_FINAL   = "#27ae60"   # jalur terpendek (hijau tua)
COLOR_HEAD    = "#e74c3c"   # kepala bergerak (merah)


class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Solver - BFS | Tugas Praktikum")
        self.root.configure(bg="#0d1b2a")
        self.root.resizable(False, False)

        canvas_w = COLS * CELL + PAD * 2
        canvas_h = ROWS * CELL + PAD * 2

        self.canvas = tk.Canvas(
            root, width=canvas_w, height=canvas_h,
            bg=COLOR_WALL, highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=(10, 0))

        # --- Panel status ---
        panel = tk.Frame(root, bg="#0d1b2a")
        panel.pack(fill="x", padx=10, pady=6)

        self.status = tk.StringVar(value="Tekan  ▶ Mulai  untuk menjalankan BFS")
        tk.Label(
            panel, textvariable=self.status,
            font=("Courier", 10), fg="#bdc3c7", bg="#0d1b2a", anchor="w"
        ).pack(side="left", padx=8)

        self.btn_reset = tk.Button(
            panel, text="↺ Reset", font=("Arial", 10, "bold"),
            bg="#c0392b", fg="white", relief="flat", padx=10, pady=4,
            cursor="hand2", command=self.reset
        )
        self.btn_reset.pack(side="right", padx=4)

        self.btn_start = tk.Button(
            panel, text="▶ Mulai", font=("Arial", 10, "bold"),
            bg="#27ae60", fg="white", relief="flat", padx=10, pady=4,
            cursor="hand2", command=self.start_animation
        )
        self.btn_start.pack(side="right", padx=4)

        # --- Legenda ---
        legend = tk.Frame(root, bg="#0d1b2a")
        legend.pack(fill="x", padx=10, pady=(0, 8))
        for color, label in [
            (COLOR_START,   "Start (S)"),
            (COLOR_END,     "Exit (E)"),
            (COLOR_VISITED, "Dieksplorasi BFS"),
            (COLOR_FINAL,   "Jalur Terpendek"),
            (COLOR_HEAD,    "Posisi Sekarang"),
        ]:
            tk.Frame(legend, bg=color, width=14, height=14).pack(side="left", padx=(6, 2))
            tk.Label(legend, text=label, font=("Arial", 9),
                     fg="#ecf0f1", bg="#0d1b2a").pack(side="left", padx=(0, 10))

        # Hitung jalur dengan BFS
        self.final_path, self.explored = bfs(MAZE, START, END)

        self.cells = {}
        self.animating = False
        self.draw_maze()

    # ----------------------------------------------------------
    def draw_maze(self):
        self.canvas.delete("all")
        self.cells = {}
        for r in range(ROWS):
            for c in range(COLS):
                x1 = PAD + c * CELL
                y1 = PAD + r * CELL
                x2 = x1 + CELL
                y2 = y1 + CELL
                ch = MAZE[r][c]
                color = {"#": COLOR_WALL, "S": COLOR_START, "E": COLOR_END}.get(ch, COLOR_PATH)

                rect = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color,
                    outline="#1e2f54", width=1
                )
                self.cells[(r, c)] = rect

                if ch in ("S", "E"):
                    self.canvas.create_text(
                        x1 + CELL // 2, y1 + CELL // 2,
                        text=ch, font=("Arial", 8, "bold"), fill="white"
                    )

    def set_cell_color(self, r, c, color):
        if (r, c) in self.cells:
            self.canvas.itemconfig(self.cells[(r, c)], fill=color)

    # ----------------------------------------------------------
    def start_animation(self):
        if self.animating:
            return
        self.animating = True
        self.btn_start.config(state="disabled")
        self.status.set("🔍 BFS sedang mengeksplorasi labirin...")

        step = [0]

        # Tahap 1: animasi eksplorasi BFS (hijau muda)
        def animate_explore():
            idx = step[0]
            if idx < len(self.explored):
                r, c = self.explored[idx]
                if MAZE[r][c] not in ("S", "E"):
                    self.set_cell_color(r, c, COLOR_VISITED)
                step[0] += 1
                pct = int((idx + 1) / len(self.explored) * 100)
                self.status.set(
                    f"🔍 Mengeksplorasi... {idx+1}/{len(self.explored)} sel  ({pct}%)"
                )
                self.root.after(30, animate_explore)
            else:
                if self.final_path:
                    self.status.set(
                        f"✅ Jalur ditemukan! Panjang: {len(self.final_path)} langkah — menandai rute..."
                    )
                else:
                    self.status.set("❌ Jalur tidak ditemukan!")
                    self.animating = False
                    self.btn_start.config(state="normal", text="▶ Jalankan Lagi")
                    return
                self.root.after(400, animate_final)

        # Tahap 2: animasi jalur terpendek (merah → hijau tua)
        def animate_final():
            path = self.final_path
            fidx = [0]

            def next_step():
                i = fidx[0]
                # Warnai sel sebelumnya jadi hijau tua (final)
                if i > 0:
                    pr, pc = path[i - 1]
                    if MAZE[pr][pc] not in ("S", "E"):
                        self.set_cell_color(pr, pc, COLOR_FINAL)
                # Warnai sel sekarang jadi merah (kepala)
                if i < len(path):
                    r, c = path[i]
                    if MAZE[r][c] not in ("S", "E"):
                        self.set_cell_color(r, c, COLOR_HEAD)
                    fidx[0] += 1
                    self.root.after(60, next_step)
                else:
                    # Pastikan sel terakhir juga hijau tua
                    lr, lc = path[-1]
                    if MAZE[lr][lc] not in ("S", "E"):
                        self.set_cell_color(lr, lc, COLOR_FINAL)
                    self.status.set(
                        f"🏁 Selesai!  Jalur terpendek: {len(path)} langkah  |  "
                        f"Total dieksplorasi: {len(self.explored)} sel"
                    )
                    self.animating = False
                    self.btn_start.config(state="normal", text="▶ Jalankan Lagi")

            next_step()

        animate_explore()

    # ----------------------------------------------------------
    def reset(self):
        if self.animating:
            self.animating = False
        self.draw_maze()
        self.btn_start.config(state="normal", text="▶ Mulai")
        self.status.set("Tekan  ▶ Mulai  untuk menjalankan BFS")


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()