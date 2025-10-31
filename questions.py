
assignments = {
    "assignment1": {
        "title": "Week 1: Assignment 1",
        "questions": [
            {
                "id": 1,
                "question": "|x+1| < 5 means",
                "options": ["-6 < x < 4", "x > 4", "x = 4", "5 < x < -6"],
                "correct_answer": 0,
                "explanation": "The inequality |x+1| < 5 means -5 < x+1 < 5, which simplifies to -6 < x < 4."
            },
            {
                "id": 2,
                "question": "If x is an irrational number, which of the following must be true?",
                "options": ["x is a real number", "x must be positive", "x is the square root of a prime number", "None of these"],
                "correct_answer": 0,
                "explanation": "All irrational numbers are real numbers, but they may not be positive or necessarily square roots of primes."
            },
            {
                "id": 3,
                "question": "(x-1)(x-2)(x-3)=0 → x=1. Which is true?",
                "options": ["The implication is true", "The converse of the implication is true", "Both the implication and its converse are true", "None of these"],
                "correct_answer": 1,
                "explanation": "The implication is false (x could be 2 or 3), but the converse 'if x=1 then (x-1)(x-2)(x-3)=0' is true."
            },
            {
                "id": 4,
                "question": "Consider the proposition 2x+5≥17. The condition x≥0 is",
                "options": ["Sufficient for the proposition to be satisfied", "Necessary for the proposition to be satisfied", "Both necessary and sufficient for the proposition to be satisfied", "Neither necessary nor sufficient for the proposition to be satisfied"],
                "correct_answer": 1,
                "explanation": "x≥0 is necessary because if x<0, 2x+5<5<17, but not sufficient since x≥6 is needed."
            },
            {
                "id": 5,
                "question": "Which of the following statements is correct?",
                "options": ["x is a rectangle → x is a square", "x² > 0 → x > 0", "xy = 0 → x = 0 or y = 0", "None of these"],
                "correct_answer": 2,
                "explanation": "If the product of two numbers is zero, at least one of them must be zero."
            },
            {
                "id": 6,
                "question": "What is the negation of the statement 'No one can help liking cats'?",
                "options": ["Some people may not like cats", "Everyone likes cats", "Some people like cats", "None of these"],
                "correct_answer": 0,
                "explanation": "The negation of 'no one likes' is 'someone does not like'."
            },
            {
                "id": 7,
                "question": "Consider the statements: (1) 'Being a square is sufficient for being a rectangle.' (2) 'Being a rectangle is necessary for being a square.' Which of these is true?",
                "options": ["Only statement (1) is true", "Only statement (2) is true", "Both (1) and (2) are true", "Neither (1) nor (2) is true"],
                "correct_answer": 2,
                "explanation": "All squares are rectangles (sufficient condition), and to be a square, you must first be a rectangle (necessary condition)."
            },
            {
                "id": 8,
                "question": "For what real number x is the following expression undefined? (x+1)(x+4)x(x+1)(x−4)",
                "options": ["x = -1 and x = 4", "x = 0, x = -1 and x = 4", "x = -1", "x = 4 and x = 0"],
                "correct_answer": 1,
                "explanation": "The expression is undefined when denominator is zero: x=0, x=-1, or x=4."
            }
        ]
    },
    "assignment2": {
        "title": "Week 2: Assignment 2",
        "questions": [
            {
                "id": 1,
                "question": "Let G = set of all graduate students in a college, and H = set of all students living in hostels. Anup belongs to the set G\\H (G minus H). It implies,",
                "options": [
                    "Anup is a college graduate student who lives in a hostel.",
                    "Anup lives in a hostel but not a college student.",
                    "Anup is a graduate student of the college who does not live in a hostel.",
                    "Anup is a non-graduate student of the college who lives in a hostel."
                ],
                "correct_answer": 2,
                "explanation": "G\\H means elements in G but not in H, so Anup is a graduate student not living in hostel."
            },
            {
                "id": 2,
                "question": "Let A = set of all Economics major students, B = set of all students taking a Mathematics course, C = set of students who play cricket. The set (A∩B)\\C denotes:",
                "options": [
                    "Economics major students who have taken Mathematics course and play cricket.",
                    "Students who have either Economics major or have taken a Mathematics course and play cricket.",
                    "Economics major students who took a Mathematics course but do not play cricket.",
                    "Students who are not Economics major but took a course in Mathematics and play cricket."
                ],
                "correct_answer": 2,
                "explanation": "(A∩B) are Economics majors taking Math, and \\C removes those who play cricket."
            },
            {
                "id": 3,
                "question": "In a village, there are 300 people. 248 are cricketers, 152 are footballers, 110 people play both cricket and football, and 42 play no sports. How many villagers play only cricket?",
                "options": ["138", "206", "96", "248"],
                "correct_answer": 0,
                "explanation": "Only cricket = Total cricketers - Both sports = 248 - 110 = 138"
            },
            {
                "id": 4,
                "question": "Total number of people who either play cricket or football but not both",
                "options": ["248", "150", "180", "258"],
                "correct_answer": 2,
                "explanation": "Cricket only (138) + Football only (42) = 180. Football only = 152 - 110 = 42"
            },
            {
                "id": 5,
                "question": "Suppose, A = {2,3,4,5}, B = {3,6,9}, C = {5,6,7,8} then (A∪B)∩(B∪C)",
                "options": ["{3,5,6,9}", "{3,5}", "{1,2}", "ϕ, the null set"],
                "correct_answer": 0,
                "explanation": "A∪B = {2,3,4,5,6,9}, B∪C = {3,5,6,7,8,9}, Intersection = {3,5,6,9}"
            },
            {
                "id": 6,
                "question": "Shreya has ₹800 income and plans to buy goods x and y priced at ₹20 and ₹10 per unit, respectively. What is Shreya's budget constraint?",
                "options": ["2x+y≤80", "2x+y≤800", "10x+20y<800", "20x+10y≥800"],
                "correct_answer": 0,
                "explanation": "Budget: 20x + 10y ≤ 800, dividing by 10 gives 2x + y ≤ 80"
            },
            {
                "id": 7,
                "question": "The budget set of Shreya, assuming x,y≥0",
                "options": [
                    "{(x,y):2x+y≤80,x≥0,y≥0}",
                    "{(x,y):20x+10y≤800, x, y ≤0}",
                    "{(x,y):x+y≤800}",
                    "{(x,y):x+2y≥800, x,y≥0}"
                ],
                "correct_answer": 0,
                "explanation": "Budget set includes all combinations satisfying budget constraint with non-negative quantities"
            },
            {
                "id": 8,
                "question": "Take the set {a, b, c, d}. Suppose you are writing down all possible subsets of this set. How many subsets are there in all?",
                "options": ["8", "10", "12", "16"],
                "correct_answer": 3,
                "explanation": "For a set with n elements, number of subsets = 2^n = 2^4 = 16"
            }
        ]
    },
    "assignment3": {
        "title": "Week 3: Assignment 3",
        "questions": [
            {
                "id": 1,
                "question": "For the function g(x) = √(x - 1), what is the domain?",
                "options": ["x≥1", "x>1", "x≤0", "x≤1"],
                "correct_answer": 0,
                "explanation": "Square root requires non-negative argument: x - 1 ≥ 0 → x ≥ 1"
            },
            {
                "id": 2,
                "question": "The population of Mathland is rising at 3.5% per year (compounded annually). Approximately how many years will it take for it to double?",
                "options": ["12", "18", "20", "25"],
                "correct_answer": 2,
                "explanation": "Using rule of 70: 70/3.5 = 20 years"
            },
            {
                "id": 3,
                "question": "A savings account with an initial deposit of 5000 rupees earns 8% interest per year (compounded annually). What is the approximate amount of savings after 6 years?",
                "options": ["6852 rupees", "7934 rupees", "8405 rupees", "None of these"],
                "correct_answer": 1,
                "explanation": "A = P(1+r)^n = 5000(1.08)^6 ≈ 7934"
            },
            {
                "id": 4,
                "question": "In a market, demand is Qd=20−2P and supply is Qs=3P. The equilibrium price and quantity are:",
                "options": ["P = 4, Q = 18", "P = 5, Q = 18", "P = 4, Q = 9", "P = 4, Q = 12"],
                "correct_answer": 3,
                "explanation": "Set Qd=Qs: 20-2P=3P → 20=5P → P=4, Q=20-2(4)=12"
            },
            {
                "id": 5,
                "question": "Suppose you draw the functions in the Q-P plane, and suppose the demand function shifts upwards by 2 units, then the new equilibrium price",
                "options": ["Rises by 3/5", "Rises by 4/5", "Rises by 2/5", "Rises by 1/5"],
                "correct_answer": 1,
                "explanation": "New demand: Qd=22-2P, set equal to Qs=3P → 22=5P → P=4.4, increase of 0.4 = 2/5"
            },
            {
                "id": 6,
                "question": "A monopolist faces the inverse demand function P = 20 − 0.5Q, and the cost function is C(Q)=2Q. At what output level is the profit of the firm maximised?",
                "options": ["10", "12", "14", "18"],
                "correct_answer": 3,
                "explanation": "MR = 20 - Q, MC = 2, set MR=MC: 20-Q=2 → Q=18"
            },
            {
                "id": 7,
                "question": "Suppose f(x) is a linear, rising function of x. Consider the function g(x)=f(x−k), where k is a constant. Which of the following is true?",
                "options": [
                    "g(x) is non-linear.",
                    "g(x) is horizontally to the right of f(x) by k",
                    "g(x) is vertically above f(x) by k.",
                    "g(x) is horizontally to the left of f(x) by k."
                ],
                "correct_answer": 1,
                "explanation": "f(x-k) represents horizontal shift to the right by k units"
            },
            {
                "id": 8,
                "question": "The reserve of natural gas in a field is given by: Q = −40t + 2000, where t=0 corresponds to January 2021, t is in years, and Q is the reserve in million cubic meters. How many million cubic meters of gas will be left in July 2024?",
                "options": ["1760", "1800", "1860", "1960"],
                "correct_answer": 2,
                "explanation": "July 2024 is t=3.5 years, Q = -40(3.5) + 2000 = -140 + 2000 = 1860"
            }
        ]
    },
    "assignment4": {
        "title": "Week 4: Assignment 4",
        "questions": [
            {
                "id": 1,
                "question": "If C(q)=20q²+100, the marginal cost at the output level of 4 units MC(4) is:",
                "options": ["40", "160", "120", "40q"],
                "correct_answer": 1,
                "explanation": "MC = dC/dq = 40q, at q=4: MC=40×4=160"
            },
            {
                "id": 2,
                "question": "Suppose the marginal cost of a firm is higher than the average cost at a particular level of output. Then the following is true:",
                "options": ["Marginal cost is rising.", "Average cost is rising.", "Total cost is rising.", "Marginal cost is higher than average cost."],
                "correct_answer": 1,
                "explanation": "When MC > AC, AC must be rising"
            },
            {
                "id": 3,
                "question": "The demand function of a mango firm is given by D(p)=200−4p², the price elasticity of demand at P=5 is:",
                "options": ["-2.5", "-2", "4", "-25"],
                "correct_answer": 1,
                "explanation": "Elasticity = (p/Q)×dQ/dp = (5/100)×(-40) = -2"
            },
            {
                "id": 4,
                "question": "At the current price 34, the market demand for a producer is 1000 and the price elasticity of demand is -2.7. A producer wants to increase his total revenue. He should,",
                "options": ["Increase the price", "Reduce the price", "Keep it intact", "None of these"],
                "correct_answer": 1,
                "explanation": "When |elasticity| > 1, reducing price increases total revenue"
            },
            {
                "id": 5,
                "question": "A country's GDP in nominal terms is growing at 9%, and the growth of the overall price level is at 3%. The real GDP growth rate is:",
                "options": ["6%", "12%", "3%", "It cannot be calculated from the given data"],
                "correct_answer": 0,
                "explanation": "Real GDP growth ≈ Nominal GDP growth - Inflation = 9% - 3% = 6%"
            },
            {
                "id": 6,
                "question": "For the production function Q(L,K)=8L⁰·⁵K⁰·⁵, find the isoquant that represents an output level of 104.",
                "options": ["L+K=139", "LK=169", "L⁰·⁵+K⁰·⁵=169", "L+K=104"],
                "correct_answer": 1,
                "explanation": "104 = 8√(LK) → √(LK) = 13 → LK = 169"
            },
            {
                "id": 7,
                "question": "The stock of capital changes over time and its behaviour is given by K(t)=12t²−t³+12. Investment at time t is",
                "options": ["16t−3t²+t", "16t−3t²", "24t²−3t", "24t−3t²+12"],
                "correct_answer": 1,
                "explanation": "I(t) = dK/dt = 24t - 3t² = 16t - 3t²"
            },
            {
                "id": 8,
                "question": "A paddy farmer has the production function: Q(L,K)=√(LK)+35L+38K. He uses L=25 units of labour and K=16 units of capital. What is the marginal product of labour and capital?",
                "options": ["1, 1", "35, 38", "1, 38", "35, 1"],
                "correct_answer": 0,
                "explanation": "MPL = ∂Q/∂L = (1/2)√(K/L) + 35 = (1/2)(4/5) + 35 = 0.4 + 35 = 35.4 ≈ 35, MPK = ∂Q/∂K = (1/2)√(L/K) + 38 = (1/2)(5/4) + 38 = 0.625 + 38 = 38.625 ≈ 38"
            }
        ]
    },
    "assignment5": {
        "title": "Week 5: Assignment 5",
        "questions": [
            {
                "id": 1,
                "question": "Suppose that C=20z−4z√(25−12x) where z is a constant and x<50. Find dC/dx.",
                "options": ["z/√(25−x²)", "−2z/√(25−12x)", "−z/√(25−x²)", "20−1/√(50−x)"],
                "correct_answer": 0,
                "explanation": "Using chain rule: dC/dx = -4z × (1/2)(25-12x)^(-1/2) × (-12) = 24z/√(25-12x)"
            },
            {
                "id": 2,
                "question": "Consider the Cobb-Douglas production function Q=f(K,L). Suppose the inputs K and L are functions of time. At a given moment, MPL=2.5, MPK=3, dK/dt=2, dL/dt=0.5. What is dQ/dt?",
                "options": ["5.5", "0", "7.25", "6"],
                "correct_answer": 2,
                "explanation": "dQ/dt = MPK×(dK/dt) + MPL×(dL/dt) = 3×2 + 2.5×0.5 = 6 + 1.25 = 7.25"
            },
            {
                "id": 3,
                "question": "Compute the third order partial derivative with respect to K from Q=4K³⁄₄L¹⁄₄",
                "options": ["−3L¹⁄₄/4K⁵⁄₄", "3L¹⁄₄/K¹⁄₄", "−15L¹⁄₄/16K⁹⁄₄", "15L¹⁄₄/16K⁹⁄₄"],
                "correct_answer": 3,
                "explanation": "∂Q/∂K = 3K^(-1/4)L^(1/4), ∂²Q/∂K² = -3/4 K^(-5/4)L^(1/4), ∂³Q/∂K³ = 15/16 K^(-9/4)L^(1/4)"
            },
            {
                "id": 4,
                "question": "For F(x,y,z)=x²y³+z²+xyz=c, use implicit function rule to find dy/dx.",
                "options": [
                    "(2xy³+yz)/(3x²y²+xz)",
                    "−(2x−yz)/(3y²+xz)",
                    "−(2xy³−yz)/(3x²y²+xz)",
                    "−(2xy³−yz−2z)/(3x²y²+xz)"
                ],
                "correct_answer": 2,
                "explanation": "dy/dx = -F_x/F_y = -(2xy³+yz)/(3x²y²+xz)"
            },
            {
                "id": 5,
                "question": "Consider Q₁=6p₁^(-2)p₂^(3/2). Estimate change in demand as p₁ and p₂ change by small amounts dp₁ and dp₂.",
                "options": [
                    "p₂^(3/2)dp₁+6p₁^(-2)dp₂",
                    "12p₂^(3/2)/p₁³ dp₁+9√p₂/p₁² dp₂",
                    "p₂/p₁³ dp₁+9p₁/√p₂ dp₂",
                    "−12√p₂/p₁³ dp₁+9√p₂/p₁² dp₂"
                ],
                "correct_answer": 3,
                "explanation": "dQ = (∂Q/∂p₁)dp₁ + (∂Q/∂p₂)dp₂ = -12p₁^(-3)p₂^(1/2)dp₁ + 9p₁^(-2)p₂^(-1/2)dp₂"
            },
            {
                "id": 6,
                "question": "Find linear approximation to F(K)=AK^α about K=1",
                "options": ["A+α(K−1)", "A[1+α(K−1)]", "Aα[1+α(K−1)]", "A[1+αK^α(K−1)]"],
                "correct_answer": 1,
                "explanation": "F(1)=A, F'(1)=Aα, so linear approx: A + Aα(K-1) = A[1+α(K-1)]"
            },
            {
                "id": 7,
                "question": "In closed economy, C=95.05+0.8Y. Estimate change in national income if investment increases by 1 unit.",
                "options": ["5", "0.8", "4", "1"],
                "correct_answer": 0,
                "explanation": "Multiplier = 1/(1-MPC) = 1/(1-0.8) = 5"
            },
            {
                "id": 8,
                "question": "From Q₁=K₁P₁^(a₁₁)P₂^(a₁₂)I^(b₁), compute cross price elasticity with respect to P₂.",
                "options": ["a₁₁", "a₁₂", "b₁", "a₁₂·K₁P₁^(a₁₁)P₂^(a₁₂−1)I^(b₁)"],
                "correct_answer": 1,
                "explanation": "Cross elasticity = (∂Q/∂P₂)×(P₂/Q) = a₁₂"
            }
        ]
    },
    "assignment6": {
        "title": "Week 6: Assignment 6",
        "questions": [
            {
                "id": 1,
                "question": "Evaluate lim(x→0) (a^x - b^x)/(e^(ax) - e^(bx)), (a≠b, a and b positive)",
                "options": ["0", "(lna-lnb)/(a-b)", "(alna-blna)/(a-b)", "No limit exists"],
                "correct_answer": 1,
                "explanation": "Using L'Hopital's rule or expansion of exponential functions"
            },
            {
                "id": 2,
                "question": "Determine values of x for which f(x)=1/√(2−x) is continuous:",
                "options": ["All real numbers", "x<2", "x≤2", "x>2"],
                "correct_answer": 1,
                "explanation": "Denominator cannot be zero and square root argument must be positive: 2-x>0 → x<2"
            },
            {
                "id": 3,
                "question": "Approximate PV of perpetuity: Rs.1000 deposits at end of each year, 14% interest rate",
                "options": ["Rs.14000", "Rs.5216", "Rs.8770", "Rs.7143"],
                "correct_answer": 3,
                "explanation": "PV = A/r = 1000/0.14 ≈ 7143"
            },
            {
                "id": 4,
                "question": "Investment earns Rs.1 lakh/year for 10 years, 9% interest. Maximum price to pay?",
                "options": ["Rs.1,00,000", "Rs.5,88,810", "Rs.6,41,800", "Rs.7,00,000"],
                "correct_answer": 2,
                "explanation": "PV = 100000 × [(1-(1.09)^(-10))/0.09] ≈ 641,800"
            },
            {
                "id": 5,
                "question": "Rs.50,000 at 7% interest. Years to double?",
                "options": ["14", "5.5", "10.24", "7.5"],
                "correct_answer": 2,
                "explanation": "Using rule: n = ln(2)/ln(1.07) ≈ 10.24 years"
            },
            {
                "id": 6,
                "question": "Find relative growth rate (1/y)(dy/dt) if y=2^(t(t²))",
                "options": ["ln2+2t", "2^t[t²ln(2+2t)]", "ln2+2t", "2tln2+2t"],
                "correct_answer": 0,
                "explanation": "ln y = t³ ln2, (1/y)(dy/dt) = 3t² ln2"
            },
            {
                "id": 7,
                "question": "House loan: Rs.50,000, 4 years, 5% interest, annual installments",
                "options": ["Approx.13200", "Approx.14800", "Approx.13850", "Approx.14100"],
                "correct_answer": 3,
                "explanation": "A = P×r/[1-(1+r)^(-n)] = 50000×0.05/[1-1.05^(-4)] ≈ 14100"
            },
            {
                "id": 8,
                "question": "Project costs 1500 now, returns 800 after 1st year, 1000 after 2nd year, 10% interest. Undertake?",
                "options": ["No", "Yes", "Cannot say", "Depends on investor"],
                "correct_answer": 1,
                "explanation": "NPV = -1500 + 800/1.1 + 1000/1.1² ≈ 34.7 > 0, so undertake"
            }
        ]
    },
    "assignment7": {
        "title": "Week 7: Assignment 7",
        "questions": [
            {
                "id": 1,
                "question": "For function f, point c in domain D is strict maximum if for all x∈D and x≠c",
                "options": ["f(x)<f(c)", "f(x)>f(c)", "f(x)≤f(c)", "f(x)≥f(c)"],
                "correct_answer": 0,
                "explanation": "Strict maximum means f(x) < f(c) for all x ≠ c"
            },
            {
                "id": 2,
                "question": "Classify stationary points of f(x)=x³+3x²−2",
                "options": [
                    "x=−2 is local min and x=0 is local max",
                    "No local extreme points exist",
                    "x=0 is local min and x=−2 is inflection point",
                    "x=0 is local min and x=−2 is local max"
                ],
                "correct_answer": 3,
                "explanation": "f'(x)=3x²+6x=3x(x+2), stationary at x=0,-2; f''(x)=6x+6; f''(0)=6>0 (min), f''(-2)=-6<0 (max)"
            },
            {
                "id": 3,
                "question": "Find extreme points of f(x)=4x²−40x+80 in [0,8]",
                "options": [
                    "x=0 min, x=8 max",
                    "x=5 min, x=8 max",
                    "x=8 min, x=5 max",
                    "x=5 min, x=0 max"
                ],
                "correct_answer": 3,
                "explanation": "f'(x)=8x-40=0 → x=5; f(0)=80, f(5)=-20, f(8)=16; so min at x=5, max at x=0"
            },
            {
                "id": 4,
                "question": "Identify incorrect statement:",
                "options": [
                    "Some extreme points are stationary points",
                    "Some stationary points are inflection points",
                    "All stationary points are extreme points",
                    "Some extreme points occur at end points"
                ],
                "correct_answer": 2,
                "explanation": "Not all stationary points are extreme points (some are inflection points)"
            },
            {
                "id": 5,
                "question": "For profit function π(L)=P·f(L)−w·L, L* is optimal if:",
                "options": [
                    "π(L*)>0 for L≤L*",
                    "π'(L*)≥0 for L≤L* and π'(L*)≤0 for L≥L*",
                    "π'(L*)≤0 for L≤L* and π'(L*)≥0 for L≥L*",
                    "π(L*)≥wL"
                ],
                "correct_answer": 1,
                "explanation": "For maximum, derivative should be ≥0 before and ≤0 after the optimal point"
            },
            {
                "id": 6,
                "question": "At optimal labour L*, which condition must be true?",
                "options": [
                    "Total revenue = total costs",
                    "Value of marginal product of labour = wage rate",
                    "Average product of labour = wage rate",
                    "Marginal product of labour = wage rate"
                ],
                "correct_answer": 1,
                "explanation": "Profit maximization requires P×MPL = w"
            },
            {
                "id": 7,
                "question": "Firm in perfect competition, P=100, C(q)=q²+2q+10, tax=8/unit. Find q* after tax",
                "options": ["49", "44", "46", "45"],
                "correct_answer": 3,
                "explanation": "After tax: P=92, MC=2q+2, set 92=2q+2 → q=45"
            },
            {
                "id": 8,
                "question": "Optimal c₁* for U=lnc₁+[1/(1+δ)]lnc₂ with incomes y₁,y₂ and interest rate r",
                "options": [
                    "c₁*=[y₂+(1+δ)y₁]/(1+r)",
                    "c₁*=(1+δ)[y₂+(1+r)y₁]/[(1+r)(2+δ)]",
                    "c₁*=(δ+1)(y₂+y₁)/[(1+r)(4+δ)]",
                    "c₁*=[y₂+(1+r)y₁]/[(1+r)(4+δ)]"
                ],
                "correct_answer": 1,
                "explanation": "From intertemporal optimization with log utility"
            }
        ]
    },
    "assignment8": {
        "title": "Week 8: Assignment 8",
        "questions": [
            {
                "id": 1,
                "question": "Find possible inflection points for f(x)=x⁶−10x⁴",
                "options": ["x=2,x=−2,x=0", "x=√(20/3),x=−√(20/3)", "x=2,x=−2", "No inflection point exists"],
                "correct_answer": 0,
                "explanation": "f''(x)=30x⁴-120x²=30x²(x²-4), changes sign at x=0,±2"
            },
            {
                "id": 2,
                "question": "Book value B(t)=√(2t) dollars, 5% continuous interest. Best time to sell?",
                "options": ["Approx.7.8 years", "Approx.5.3 years", "Sell immediately", "Approx.48.05 years"],
                "correct_answer": 3,
                "explanation": "Maximize present value: B(t)e^(-0.05t), solve dB/dt = rB"
            },
            {
                "id": 3,
                "question": "In perfect competition, sufficient condition for profit maximization:",
                "options": [
                    "Marginal cost equals price",
                    "Marginal cost curve has negative slope",
                    "Marginal cost equals zero",
                    "Marginal cost curve has positive slope"
                ],
                "correct_answer": 3,
                "explanation": "MC = P is necessary, MC rising (positive slope) is sufficient"
            },
            {
                "id": 4,
                "question": "Find x₀>0 minimizing f(x)=I₀+Kx+Ae^(-αx) given Aα>K",
                "options": ["(1/α)ln(Kα/A)", "−(1/α)ln(αA/K)", "(1/α)ln(αA/K)", "−(1/α)ln(K/A)"],
                "correct_answer": 2,
                "explanation": "f'(x)=K-αAe^(-αx)=0 → e^(αx)=αA/K → x=(1/α)ln(αA/K)"
            },
            {
                "id": 5,
                "question": "Find fertilizer amount maximizing profit: Y(N)=−13.62+0.984N−0.05N^1.5, wheat=$1.40, fertilizer=$0.18",
                "options": ["Approx.110", "Approx.130", "Approx.100", "Approx.140"],
                "correct_answer": 1,
                "explanation": "Maximize 1.4Y(N)-0.18N, solve first order condition"
            },
            {
                "id": 6,
                "question": "Firm: P=121, C(Q)=0.02Q³−3Q²+175Q+500, Q≤110. Profit maximizing Q?",
                "options": ["10", "110", "0", "90"],
                "correct_answer": 3,
                "explanation": "MR=121, MC=0.06Q²-6Q+175, set equal and check boundary"
            },
            {
                "id": 7,
                "question": "Monopoly: P(Q)=100−Q/3, C(Q)=(1600Q/3)−(Q²/3)+50Q+1000/3. Profit maximizing Q?",
                "options": ["100", "0", "300", "10"],
                "correct_answer": 0,
                "explanation": "Set MR=MC and solve"
            },
            {
                "id": 8,
                "question": "C(Q)=2Q²+10Q+32, Q>0. Find Q minimizing average cost",
                "options": ["2", "8", "4", "√32"],
                "correct_answer": 2,
                "explanation": "AC=2Q+10+32/Q, minimize: d(AC)/dQ=2-32/Q²=0 → Q=4"
            }
        ]
    },
    "assignment9": {
        "title": "Week 9: Assignment 9",
        "questions": [
            {
                "id": 1,
                "question": "In ∫f(x)dx=F(x)+C, which is called integrand?",
                "options": ["F(x)", "f(x)", "C", "None of these"],
                "correct_answer": 1,
                "explanation": "f(x) is the integrand, the function being integrated"
            },
            {
                "id": 2,
                "question": "∫e^(1 ln x) dx =",
                "options": ["ln|e|+C", "1", "0", "e"],
                "correct_answer": 1,
                "explanation": "e^(ln x) = x, ∫x dx = x²/2 + C, but e^(1 ln x) = e^(ln x) = x"
            },
            {
                "id": 3,
                "question": "If ∫(-4 to 2)g(x)dx=8 and ∫(-4 to 0)g(x)dx=6, find ∫(0 to 2)g(x)dx",
                "options": ["6", "5", "2", "4"],
                "correct_answer": 2,
                "explanation": "∫(0 to 2) = ∫(-4 to 2) - ∫(-4 to 0) = 8 - 6 = 2"
            },
            {
                "id": 4,
                "question": "If ∫f(x)dx=F(x)+C, then d/dt ∫(t to a)f(x)dx =",
                "options": ["F(x)", "F(t)", "f(t)", "F(a)"],
                "correct_answer": 2,
                "explanation": "By Fundamental Theorem of Calculus"
            },
            {
                "id": 5,
                "question": "Find F(x) with F'(x)=3(x+1)² passing through (1,2)",
                "options": ["x²−x/x³−x+4", "x³+3/2x²+3x−6", "x³+3x²+3x−5", "x³+1/3x²+2x−5"],
                "correct_answer": 2,
                "explanation": "F(x)=∫3(x+1)²dx=(x+1)³+C=x³+3x²+3x+1+C, use F(1)=2 to find C=-5"
            },
            {
                "id": 6,
                "question": "Marginal cost=3q²+2q+5, fixed cost=100. Average cost?",
                "options": ["q²+q+5+100/q", "q²+q+100", "q³+q²/2+10q+5", "3q+1+2q"],
                "correct_answer": 0,
                "explanation": "TC=∫MC dq + FC=q³+q²+5q+100, AC=TC/q=q²+q+5+100/q"
            },
            {
                "id": 7,
                "question": "If f(x) is income density function, then ∫(a to b)f(x)dx represents",
                "options": ["Income between a and b", "Income above b", "Proportion of total income between a and b", "Proportion of people with income between a and b"],
                "correct_answer": 3,
                "explanation": "For density function, integral gives proportion/probability"
            },
            {
                "id": 8,
                "question": "K(t) with I(t)=4t²+3t, K(0)=50. Find K(4)",
                "options": ["≈179", "≈185", "≈205", "≈159"],
                "correct_answer": 3,
                "explanation": "K(t)=∫I(t)dt+K(0)=(4t³/3)+(3t²/2)+50, at t=4: (256/3)+24+50≈159"
            }
        ]
    },
    "assignment10": {
        "title": "Week 10: Assignment 10",
        "questions": [
            {
                "id": 1,
                "question": "Sample question 1 for assignment 10",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 0,
                "explanation": "Explanation for question 1"
            },
            {
                "id": 2,
                "question": "Sample question 2 for assignment 10",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 1,
                "explanation": "Explanation for question 2"
            },
            # Add remaining 6 questions for assignment 10 following the same pattern
            {
                "id": 3,
                "question": "Sample question 3 for assignment 10",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 2,
                "explanation": "Explanation for question 3"
            },
            {
                "id": 4,
                "question": "Sample question 4 for assignment 10",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 3,
                "explanation": "Explanation for question 4"
            },
            {
                "id": 5,
                "question": "Sample question 5 for assignment 10",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 0,
                "explanation": "Explanation for question 5"
            },
            {
                "id": 6,
                "question": "Sample question 6 for assignment 10",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 1,
                "explanation": "Explanation for question 6"
            },
            {
                "id": 7,
                "question": "Sample question 7 for assignment 10",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 2,
                "explanation": "Explanation for question 7"
            },
            {
                "id": 8,
                "question": "Sample question 8 for assignment 10",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_answer": 3,
                "explanation": "Explanation for question 8"
            }
        ]
    }
}

def get_all_assignments():
    return assignments

def get_assignment(assignment_id):
    return assignments.get(assignment_id)

def calculate_score(assignment_id, user_answers):
    assignment = assignments.get(assignment_id)
    if not assignment:
        return 0, 0
    
    correct_count = 0
    total_questions = len(assignment["questions"])
    
    for question in assignment["questions"]:
        q_id = str(question["id"])
        if q_id in user_answers and user_answers[q_id] == question["correct_answer"]:
            correct_count += 1
    
    return correct_count, total_questions