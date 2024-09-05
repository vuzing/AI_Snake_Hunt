import pygame
import heapq
import random
import time
from collections import deque

# Khởi tạo pygame
pygame.init()

# Kích thước ô vuông và kích thước mê cung
CELL_SIZE = 20
MAZE_WIDTH, MAZE_HEIGHT = 50, 25
MENU_WIDTH = 250

# Kích thước mê cung và menu
total_maze_width = MAZE_WIDTH * CELL_SIZE
total_menu_width = MENU_WIDTH
total_height = MAZE_HEIGHT * CELL_SIZE

# Tính toán kích thước cửa sổ
WINDOW_WIDTH = total_maze_width + total_menu_width
WINDOW_HEIGHT = total_height

# Đảm bảo cửa sổ có kích thước tối thiểu
MIN_WINDOW_WIDTH = 1400
MIN_WINDOW_HEIGHT = 650
WINDOW_WIDTH = max(WINDOW_WIDTH, MIN_WINDOW_WIDTH)
WINDOW_HEIGHT = max(WINDOW_HEIGHT, MIN_WINDOW_HEIGHT)

# Tính khoảng cách từ lề cửa sổ đến mê cung và menu
margin_x = (WINDOW_WIDTH - total_maze_width - total_menu_width) // 2
margin_y = (WINDOW_HEIGHT - total_height) // 2

# Khởi tạo cửa sổ
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Real-Time Maze Solver')

# Load the background image and scale it to fit the window size
BACKGROUND_IMAGE = pygame.image.load(r'WINDOWS.png').convert()
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Inside your game loop, before any other drawing code
screen.blit(BACKGROUND_IMAGE, (0, 0))

#Gán ảnh cho các ô và nút

WHITE = pygame.image.load(r'wall.png').convert() # Tường
PINK =  pygame.image.load(r'MENU.jpg').convert() # Menu
RED =  pygame.image.load(r'start.png').convert()     # Xuất phát
GREEN =  pygame.image.load(r'finish.png').convert() # Đích đến
BLACK =  pygame.image.load(r'path.png').convert() # ĐƯỜNG CÓ THỂ ĐI
BLUE =  pygame.image.load(r'smoke.png').convert()    # Đường duyệt
YELLOW = pygame.image.load(r'solution.png').convert() # Đường giải
GRAY = (247, 171, 5)  # Nút bấm
GRAY1 = (247, 100, 5)




player_image = pygame.image.load(r'smoke.png').convert_alpha()


# Hàm để vẽ ô vuông
def draw_cell(image, x, y):
    screen.blit(image, (x * CELL_SIZE + margin_x, y * CELL_SIZE + margin_y))


# Định nghĩa các nút
button_start = pygame.Rect(WINDOW_WIDTH // 2 - 75, WINDOW_HEIGHT // 3, 150, 50)
button_exit = pygame.Rect(WINDOW_WIDTH // 2 - 75, WINDOW_HEIGHT // 2, 150, 50)
button_back = pygame.Rect(WINDOW_WIDTH // 2 - 600, WINDOW_HEIGHT - 630, 150, 50)
button_generate = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 140, 125, 40)
button_generate_easy = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 190, 125, 40)
button_solve_bfs = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 240, 125, 40)
button_solve_dfs = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 290, 125, 40)
button_solve_ucs = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 340, 125, 40)
button_solve_dijkstra = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 390, 125, 40)
button_solve_astar = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 440, 125, 40)
button_solve_greedy = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 490, 125, 40)
button_player = pygame.Rect((MAZE_WIDTH * CELL_SIZE) + 140, 540, 125, 40)



START_IMAGE = pygame.image.load(r'STARTGAME.png').convert_alpha()
EXIT_IMAGE = pygame.image.load(r'EXIT.png').convert_alpha()
BACK_IMAGE = pygame.image.load(r'BACK.png').convert_alpha()
BUTTON_IMAGE_1 = pygame.image.load(r'MAZE1.png').convert_alpha()
BUTTON_IMAGE_2 = pygame.image.load(r'MAZE2.png').convert_alpha()
BUTTON_IMAGE_3 = pygame.image.load(r'BFS.png').convert_alpha()
BUTTON_IMAGE_4 = pygame.image.load(r'DFS.png').convert_alpha()
BUTTON_IMAGE_5 = pygame.image.load(r'UCS.png').convert_alpha()
BUTTON_IMAGE_6 = pygame.image.load(r'DIJKSTRA.png').convert_alpha()
BUTTON_IMAGE_7 = pygame.image.load(r'ASTAR.png').convert_alpha()
BUTTON_IMAGE_8 = pygame.image.load(r'GREEDY.png').convert_alpha()
PLAYER_BUTTON_IMAGE = pygame.image.load(r'MAZE2.png').convert_alpha()


START_IMAGE = pygame.transform.scale(START_IMAGE, (150, 50))
EXIT_IMAGE = pygame.transform.scale(EXIT_IMAGE, (150, 50))
BACK_IMAGE = pygame.transform.scale(BACK_IMAGE, (150, 50))
WHITE = pygame.transform.scale(WHITE, (CELL_SIZE, CELL_SIZE))
PINK = pygame.transform.scale(PINK, (CELL_SIZE, CELL_SIZE))
RED = pygame.transform.scale(RED, (CELL_SIZE, CELL_SIZE))
GREEN = pygame.transform.scale(GREEN, (CELL_SIZE, CELL_SIZE))
BLACK = pygame.transform.scale(BLACK, (CELL_SIZE, CELL_SIZE))
BLUE = pygame.transform.scale(BLUE, (CELL_SIZE, CELL_SIZE))
YELLOW = pygame.transform.scale(YELLOW, (CELL_SIZE, CELL_SIZE))
#GRAY = pygame.transform.scale(PINK, (CELL_SIZE, CELL_SIZE))
player_image = pygame.transform.scale(player_image, (CELL_SIZE, CELL_SIZE))

BUTTON_IMAGE_1 = pygame.transform.scale(BUTTON_IMAGE_1, (125, 40))  # Size of the button
BUTTON_IMAGE_2 = pygame.transform.scale(BUTTON_IMAGE_2, (125, 40))
BUTTON_IMAGE_3 = pygame.transform.scale(BUTTON_IMAGE_3, (125, 40))
BUTTON_IMAGE_4 = pygame.transform.scale(BUTTON_IMAGE_4, (125, 40))
BUTTON_IMAGE_5 = pygame.transform.scale(BUTTON_IMAGE_5, (125, 40))
BUTTON_IMAGE_6 = pygame.transform.scale(BUTTON_IMAGE_6, (125, 40))
BUTTON_IMAGE_7 = pygame.transform.scale(BUTTON_IMAGE_7, (125, 40))
BUTTON_IMAGE_8 = pygame.transform.scale(BUTTON_IMAGE_8, (125, 40))
PLAYER_BUTTON_IMAGE = pygame.transform.scale(PLAYER_BUTTON_IMAGE, (125, 40))

# Hàm vẽ các nút
def draw_button(button, image):
    # Blit the image at the position of the button
    screen.blit(image, button.topleft)

# Vẽ menu
def draw_menu():
    # Calculate the menu background size
    menu_background_width = 0
    menu_background_height = 0 * 0

    # Scale the PINK image to the size of the menu background
    menu_background_image = pygame.transform.scale(PINK, (menu_background_width, menu_background_height))

    # Draw the menu background image
    menu_img_position = (total_maze_width + margin_x, margin_y)
    screen.blit(menu_background_image, menu_img_position)

    # Draw the buttons with their respective images
    draw_button(button_generate, BUTTON_IMAGE_1)
    draw_button(button_generate_easy, BUTTON_IMAGE_2)
    draw_button(button_solve_bfs, BUTTON_IMAGE_3)
    draw_button(button_solve_dfs, BUTTON_IMAGE_4)
    draw_button(button_solve_ucs, BUTTON_IMAGE_5)
    draw_button(button_solve_dijkstra, BUTTON_IMAGE_6)
    draw_button(button_solve_astar, BUTTON_IMAGE_7)
    draw_button(button_solve_greedy, BUTTON_IMAGE_8)
#    draw_button(button_player, PLAYER_BUTTON_IMAGE)
    
    pygame.display.flip()

#maze_created = False

def draw_welcome_screen():
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    screen.blit(START_IMAGE, button_start.topleft)
    screen.blit(EXIT_IMAGE, button_exit.topleft)
    pygame.display.flip()
def draw_main_screen():
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    draw_menu()
    screen.blit(BACK_IMAGE, button_back.topleft)
    pygame.display.flip()

def initialize_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    return maze

def get_random_edge_cell(width, height):
    # Chọn cạnh: 0 = trên, 1 = phải, 2 = dưới, 3 = trái
    edge = random.randint(0, 3)
    if edge == 0:  # Cạnh trên
        return (random.randint(1, width - 2), 0)
    elif edge == 1:  # Cạnh phải
        return (width - 1, random.randint(1, height - 2))
    elif edge == 2:  # Cạnh dưới
        return (random.randint(1, width - 2), height - 1)
    else:  # Cạnh trái
        return (0, random.randint(1, height - 2))

def opposite_edge(cell, width, height):
    x, y = cell
    if x == 0:
        return (width - 1, random.randint(1, height - 2))
    elif x == width - 1:
        return (0, random.randint(1, height - 2))
    elif y == 0:
        return (random.randint(1, width - 2), height - 1)
    else:
        return (random.randint(1, width - 2), 0)

start = None
end = None
path_length = 0       # Độ dài của lộ trình
start_time = 0        # Thời gian bắt đầu giải mê cung
end_time = 0          # Thời gian kết thúc giải mê cung

 
# Tạo mê cung ngẫu nhiên theo thời gian thực
def generate_maze(width, height, open_wall_rate=0.08):
    global start, end
    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:  # Tăng khoảng cách giữa các ô
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                neighbors.append((nx, ny))
        return neighbors

    def can_be_extended(x, y):
        # Kiểm tra xem ô có thể mở rộng mà không tạo ra nhánh cụt ngắn không
        count = 0
        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            nx, ny = x + dx*2, y + dy*2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                count += 1
        return count <= 1  # Chỉ mở rộng nếu có 1 hoặc không có ô đã mở rộng xung quanh


    def carve_passage_from(x, y, maze, visited, width, height):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < width) and (0 <= ny < height) and (maze[ny][nx] == 1):
                between_x, between_y = (x + nx) // 2, (y + ny) // 2
                if not visited.get((nx, ny), False):
                    maze[between_y][between_x] = 0
                    maze[ny][nx] = 0
                    visited[(nx, ny)] = True
                    update_display(maze, width, height, start, end)  # Update the display as you carve
                    carve_passage_from(nx, ny, maze, visited, width, height)  # Recursive call
    
               
    maze = [[1 for _ in range(width)] for _ in range(height)]
    start = get_random_edge_cell(width, height)
    end = opposite_edge(start, width, height)
    visited = {(start[0], start[1]): True}
    maze[start[1]][start[0]] = 0
    
    

    carve_passage_from(start[0], start[1], maze, visited, width, height)

    maze[end[1]][end[0]] = 0
    
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1 and random.random() < open_wall_rate:  # Kiểm tra nếu là tường và áp dụng tỷ lệ
                maze[y][x] = 0  # Chuyển ô tường thành đường đi
    update_display(maze, width, height, start, end)

    return maze

def generate_maze_easy(width, height):
    global start, end, maze_created

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                neighbors.append((nx, ny))
        return neighbors

    def add_frontiers(x, y, frontiers):
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                frontiers.add((nx, ny))

    maze = [[1 for _ in range(width)] for _ in range(height)]

    start = get_random_edge_cell(width, height)
    end = opposite_edge(start, width, height)
    maze[start[1]][start[0]] = 0

    frontiers = set()
    add_frontiers(start[0], start[1], frontiers)

    while frontiers:
        x, y = random.choice(list(frontiers))
        frontiers.remove((x, y))
        maze[y][x] = 0

        neighbors = get_neighbors(x, y)
        connected_neighbors = [n for n in neighbors if maze[n[1]][n[0]] == 0]

        if connected_neighbors:
            nx, ny = random.choice(connected_neighbors)
            maze[(y + ny) // 2][(x + nx) // 2] = 0

        add_frontiers(x, y, frontiers)
        update_display(maze, width, height, start, end)

    maze[end[1]][end[0]] = 0
    update_display(maze, width, height, start, end)
    maze_created = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()  # Sử dụng sys.exit() thay vì exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Kiểm tra xem click có nằm trong khu vực menu không
                if x > total_maze_width + 100 and x > total_height + 100:  # Giả sử total_maze_width là chiều rộng của phần mê cung
                    running = False
                    break  # Thoát khỏi vòng lặp while
                else:
                    handle_maze_click(event, maze)

    return maze

def update_display(maze, width, height, start, end):
    for y in range(height):
        for x in range(width):
            cell_image = BLACK if maze[y][x] == 0 else WHITE
            draw_cell(cell_image, x, y)

    draw_cell(RED,start[0], start[1])  # Vẽ lối vào
    draw_cell(GREEN, end[0], end[1] )  # Vẽ lối ra
    pygame.display.flip()
    time.sleep(0.01)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def display_message(text, color, position):
    font = pygame.font.SysFont('Arial', 36)
    text_surface = font.render(text, True, (245, 66, 93))
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
  
vertices_visited = 0  # Số đỉnh đã duyệt    

# Hàm để thực hiện một bước BFS
def add_neighbors_to_queue(maze, queue, current, prev, visited, end):
    global vertices_visited

    x, y = current
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_x, next_y = x + direction[0], y + direction[1]
        if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze) and \
           maze[next_y][next_x] == 0 and (next_x, next_y) not in visited:
            queue.append((next_x, next_y))
            prev[(next_x, next_y)] = current
            visited.add((next_x, next_y))
            vertices_visited += 1
            if (next_x, next_y) != end:  # Không vẽ lại ô đích
                draw_cell(BLUE,next_x, next_y)  # Vẽ màu cho ô mới
                pygame.display.flip()  # Cập nhật màn hình
                time.sleep(0.01)  # Điều chỉnh tốc độ hiển thị

def bfs_step(maze, queue, prev, visited, end):
    global start_time, end_time
    if not queue:
        return True, False  # Queue rỗng, không tìm thấy lời giải

    if queue[0] == start:  # Bắt đầu tính thời gian khi bắt đầu từ điểm xuất phát
        start_time = time.time()

    current = queue.popleft()

    if current == end:
        end_time = time.time()  # Dừng đo thời gian khi tìm thấy lối ra
        return True, True  # Tìm thấy lời giải

    add_neighbors_to_queue(maze, queue, current, prev, visited, end)
    return False, False  # BFS vẫn đang tiếp diễn

def dfs_step(maze, stack, prev, visited, end):
    global vertices_visited, start_time, end_time

    if not stack:
        return True, False

    if stack[-1] == start:  # Bắt đầu tính thời gian từ điểm xuất phát
        start_time = time.time()

    current = stack.pop()

    if current == end:
        end_time = time.time()  # Kết thúc tính thời gian khi tìm thấy lời giải
        return True, True  # Tìm thấy lời giải
    vertices_visited += 1
    x, y = current
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_x, next_y = x + direction[0], y + direction[1]
        if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze) and \
           maze[next_y][next_x] == 0 and (next_x, next_y) not in visited:
            stack.append((next_x, next_y))
            prev[(next_x, next_y)] = current
            visited.add((next_x, next_y))
            if (next_x, next_y) != end:  # Kiểm tra để không vẽ lại ô đích
                draw_cell(BLUE, next_x, next_y)  # Vẽ màu cho ô mới
                pygame.display.flip()  # Cập nhật màn hình
                time.sleep(0.01)  # Điều chỉnh tốc độ hiển thị

    return False, False  # DFS vẫn đang tiếp diễn

def ucs_step(maze, priority_queue, prev, visited, cost, end):
    global vertices_visited, start_time, end_time

    if not priority_queue:
        return True, False

    if priority_queue[0][1] == start:
        start_time = time.time()

    current_cost, current = heapq.heappop(priority_queue)

    if current == end:
        end_time = time.time()
        return True, True

    x, y = current
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_x, next_y = x + direction[0], y + direction[1]
        if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze) and \
           maze[next_y][next_x] == 0 and (next_x, next_y) not in visited:
            next_cost = current_cost + 1
            heapq.heappush(priority_queue, (next_cost, (next_x, next_y)))
            prev[(next_x, next_y)] = current
            cost[(next_x, next_y)] = next_cost
            visited.add((next_x, next_y))
            vertices_visited += 1
            if (next_x, next_y) != end:
                draw_cell(BLUE, next_x, next_y)
                pygame.display.flip()
                time.sleep(0.01)

    return False, False

def dijkstra_step(maze, priority_queue, prev, visited, cost, end):
    global vertices_visited, start_time, end_time

    if not priority_queue:
        return True, False

    if priority_queue[0][1] == start:
        start_time = time.time()

    current_cost, current = heapq.heappop(priority_queue)

    if current == end:
        end_time = time.time()
        return True, True

    x, y = current
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_x, next_y = x + direction[0], y + direction[1]
        if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze) and \
           maze[next_y][next_x] == 0 and (next_x, next_y) not in visited:
            next_cost = current_cost + 1
            if next_cost < cost.get((next_x, next_y), float('inf')):
                heapq.heappush(priority_queue, (next_cost, (next_x, next_y)))
                prev[(next_x, next_y)] = current
                cost[(next_x, next_y)] = next_cost
                visited.add((next_x, next_y))
                vertices_visited += 1
                if (next_x, next_y) != end:
                    draw_cell(BLUE, next_x, next_y)
                    pygame.display.flip()
                    time.sleep(0.01)

    return False, False
# Hàm heuristic (khoảng cách Manhattan)
def heuristic(cell, end):
    return abs(cell[0] - end[0]) + abs(cell[1] - end[1])


# Define a cutoff for the heuristic cost.
HEURISTIC_CUTOFF = 10  # This value is arbitrary and should be chosen based on your specific use case.

# Hàm thực hiện bước tiếp theo của A*
def astar_step(maze, priority_queue, prev, visited, cost, end):
    global vertices_visited, start_time, end_time

    if not priority_queue:  
        return True, False

    if priority_queue[0][1] == start:
        start_time = time.time()

    current_cost, current = heapq.heappop(priority_queue)

    if current == end:
        end_time = time.time()
        return True, True

    vertices_visited += 1

    x, y = current
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_x, next_y = x + direction[0], y + direction[1]
        if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze) and \
           maze[next_y][next_x] == 0 and (next_x, next_y) not in visited:
            next_cost = current_cost + 1
            h_cost = heuristic((next_x, next_y), end)
            total_cost = next_cost + h_cost

            if (next_x, next_y) not in cost or total_cost < cost.get((next_x, next_y), float('inf')):
                heapq.heappush(priority_queue, (total_cost, (next_x, next_y)))
                prev[(next_x, next_y)] = current
                cost[(next_x, next_y)] = next_cost
                if (next_x, next_y) != end:
                    draw_cell(BLUE, next_x, next_y)
                    pygame.display.flip()
                    time.sleep(0.01)

    return False, False

def greedy_step(maze, priority_queue, prev, visited, end):
    global vertices_visited, start_time, end_time

    if not priority_queue:
        return True, False

    if priority_queue[0][1] == start:
        start_time = time.time()

    _, current = heapq.heappop(priority_queue)

    if current == end:
        end_time = time.time()
        return True, True

    vertices_visited += 1

    x, y = current
    for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_x, next_y = x + direction[0], y + direction[1]
        if 0 <= next_x < len(maze[0]) and 0 <= next_y < len(maze) and \
           maze[next_y][next_x] == 0 and (next_x, next_y) not in visited:
            h_cost = heuristic((next_x, next_y), end)
            heapq.heappush(priority_queue, (h_cost, (next_x, next_y)))
            prev[(next_x, next_y)] = current
            visited.add((next_x, next_y))
            if (next_x, next_y) != end:
                draw_cell(BLUE, next_x, next_y)
                pygame.display.flip()
                time.sleep(0.01)

    return False, False # Greedy vẫn đang tiếp diễn

def handle_mouse_events_welcome_screen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_start.collidepoint(event.pos):
                return 'start'
            elif button_exit.collidepoint(event.pos):
                return 'exit'
    return None

# Hàm xử lý sự kiện chuột, trả về tên thuật toán giải nếu có
def handle_mouse_events_main_screen():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'quit'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_generate.collidepoint(event.pos):
                return 'generate 1'
            if button_generate_easy.collidepoint(event.pos):
                return 'generate 2'
            elif button_solve_bfs.collidepoint(event.pos):
                return 'bfs'
            elif button_solve_dfs.collidepoint(event.pos):
                return 'dfs'
            elif button_solve_ucs.collidepoint(event.pos):
                return 'ucs'
            elif button_solve_dijkstra.collidepoint(event.pos):
                return 'dijkstra'
            elif button_solve_astar.collidepoint(event.pos):  # Nút mới
                return 'astar'
            elif button_solve_greedy.collidepoint(event.pos):
                return 'greedy'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.collidepoint(event.pos):
                    return 'back'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_player.collidepoint(event.pos):
                    return 'player_mode'
            
    return None

# Hàm khởi tạo các biến cho thuật toán tìm kiếm
def initialize_search(algorithm):
    global queue, stack, priority_queue, prev, visited, solved, start, end, cost, start_time, vertices_visited
    vertices_visited = 0  # Đặt lại số đỉnh đã duyệt
    start_time = time.time()  # Ghi nhận thời gian bắt đầu giải mê cung
    prev = {start: None}
    visited = {start}
    solved = False

    if algorithm == 'bfs':
        queue = deque([start])  # Khởi tạo queue cho BFS
    elif algorithm == 'dfs':
        stack = [start]         # Khởi tạo stack cho DFS
    elif algorithm in ['ucs', 'dijkstra', 'astar']:
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))  # Khởi tạo hàng đợi ưu tiên
        cost = {start: 0}
    elif algorithm == 'greedy':
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))
        
        
        
# Hàm đặt lại mê cung về trạng thái chưa giải      
def reset_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 0:  # Kiểm tra nếu ô hiện tại là đường đi
                if (x, y) != start and (x, y) != end:  # Bỏ qua ô xuất phát và ô đích
                    draw_cell(BLACK, x, y)  # Chuyển thành màu đen

    pygame.display.flip()
    
# Hàm giải mê cung với thuật toán được chọn
def solve_maze(maze, algorithm):
    global solved, path_length, start_time, end_time

    if not solved:
        if algorithm == 'bfs':
            solved, found_solution = bfs_step(maze, queue, prev, visited, end)
        elif algorithm == 'dfs':
            solved, found_solution = dfs_step(maze, stack, prev, visited, end)
        elif algorithm == 'ucs':
            solved, found_solution = ucs_step(maze, priority_queue, prev, visited, cost, end)
        elif algorithm == 'dijkstra':
            solved, found_solution = dijkstra_step(maze, priority_queue, prev, visited, cost, end)
        elif algorithm == 'astar':  # Xử lý A*
            solved, found_solution = astar_step(maze, priority_queue, prev, visited, cost, end)
        elif algorithm == 'greedy':
            solved, found_solution = greedy_step(maze, priority_queue, prev, visited, end)
        if solved:
            if found_solution:
                draw_solution_path(prev, start, end)
                time_elapsed = end_time - start_time
                display_maze_info(time_elapsed, path_length)
            else:
                display_message("", RED, ((MAZE_WIDTH * CELL_SIZE) + MENU_WIDTH // 2, MAZE_HEIGHT * CELL_SIZE // 2))

info_surface = pygame.Surface((900,50)) # đặt kích thước phù hợp
info_surface_rect = info_surface.get_rect(topleft=(150, 590))  # Đặt vị trí

def clear_info_surface():
    info_surface.fill((255,255,255))  # Sử dụng màu nền phù hợp

def display_maze_info(time_elapsed, path_length):
    global vertices_visited
    clear_info_surface()  # Xóa nội dung cũ trên Surface
    info_text = f"Thoi gian giai: {time_elapsed:.2f}s, Do dai duong di: {path_length}, So dinh da duyet: {vertices_visited}"
    font = pygame.font.SysFont('Arial', 36)
    text_surface = font.render(info_text, True, (0,0,0))  # BLACK là màu chữ
    info_surface.blit(text_surface, (10, 10))  # Vị trí text trong Surface
    screen.blit(info_surface, info_surface_rect)  # Hiển thị Surface lên màn hình
    pygame.display.flip()
def reset_info():
    global vertices_visited, start_time, end_time
    vertices_visited = 0
    start_time = 0
    end_time = 0
    # Xóa thông tin hiển thị cũ trên màn hình
# Hàm vẽ lộ trình giải quyết
def draw_solution_path(prev, start, end):
    global path_length
    current = prev[end]
    path_length = 0
    while current != start:
        path_length += 1  # Tăng độ dài đường đi
        x, y = current
        draw_cell(YELLOW, x, y)
        current = prev[current]
        pygame.display.flip()
        time.sleep(0.01)

    draw_cell(RED, start[0], start[1])   # Vẽ lại ô xuất phát
    draw_cell(GREEN, end[0], end[1])     # Vẽ lại ô đích

# Hàm xử lý sự kiện di chuyển trong chế độ người chơi
def handle_player_movement(event, maze):
    global player_position, path_length
    x, y = player_position

    new_x, new_y = x, y  # Giữ nguyên vị trí nếu không có di chuyển

    if event.key == pygame.K_LEFT:
        new_x = x - 1
    elif event.key == pygame.K_RIGHT:
        new_x = x + 1
    elif event.key == pygame.K_UP:
        new_y = y - 1
    elif event.key == pygame.K_DOWN:
        new_y = y + 1

    # Kiểm tra vị trí mới có nằm trong giới hạn của mê cung và là đường đi
    if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT and maze[new_y][new_x] == 0:
        draw_cell(YELLOW, x, y)  # Vẽ lại ô cũ màu vàng
        player_position = (new_x, new_y)  # Cập nhật vị trí mới
        draw_cell(player_image, new_x, new_y)  # Vẽ người chơi ở vị trí mới
        path_length += 1
        pygame.display.flip()
        return True

    return False

def handle_maze_click(event, maze):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        grid_x = (x - margin_x) // CELL_SIZE
        grid_y = (y - margin_y) // CELL_SIZE

        if 0 <= grid_x < MAZE_WIDTH and 0 <= grid_y < MAZE_HEIGHT:
            if maze[grid_y][grid_x] == 0:  # Nếu là ô đường đi
                maze[grid_y][grid_x] = 1  # Chuyển thành ô tường
                draw_cell(WHITE, grid_x, grid_y)  # Vẽ lại ô đó
                pygame.display.flip()

def main():
    global solved, start, end, found_solution, player_mode, player_position, start_time, path_length, maze_created
    clock = pygame.time.Clock()
    maze = []
    algorithm = None
    running = True
    show_welcome_screen = True
    maze_created = False
    player_mode = False

    while running:
        if show_welcome_screen:
            draw_welcome_screen()
            action = handle_mouse_events_welcome_screen()
            if action == 'quit':
                running = False
            elif action == 'start':
                show_welcome_screen = False
                draw_main_screen()
            elif action == 'exit':
                running = False
        else:
            action = handle_mouse_events_main_screen()
            if action == 'quit':
                running = False
            elif action == 'back':
                show_welcome_screen = True
            elif action == 'generate 1':
                maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT, 0.08)
                maze_created = True
            elif action == 'generate 2':
                maze = generate_maze_easy(MAZE_WIDTH, MAZE_HEIGHT)
                maze_created = True
            elif action in ['bfs', 'dfs', 'ucs', 'dijkstra', 'astar', 'greedy'] and maze_created:
                reset_info()
                algorithm = action
                reset_maze(maze)
                initialize_search(algorithm)
            elif action == 'player_mode' and maze_created:
                player_mode = True
                player_position = start
                reset_maze(maze)
                draw_cell(player_image, start[0], start[1])
                pygame.display.flip()

        if maze_created and not algorithm:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    handle_maze_click(event, maze)

        if algorithm:
            solve_maze(maze, algorithm)

        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

