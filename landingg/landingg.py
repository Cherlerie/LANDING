import reflex as rx

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        features(),
        pricing(),
        faq(),
        footer(),
        bg="linear-gradient(to bottom, #1a202c, #2d3748)",  # fondo degradado
        min_height="100vh"
    )


def navbar() -> rx.Component:
    return rx.hstack(
        rx.heading("ECLIPSE", size="5", color="white", font_weight="bold"),
        rx.spacer(),
        rx.hstack(
            rx.link("Features", href="#features", color="gray.300", _hover={"color": "white"}),
            rx.link("Pricing", href="#pricing", color="gray.300", _hover={"color": "white"}),
            rx.link("FAQs", href="#faq", color="gray.300", _hover={"color": "white"}),  # ← este era #faqs
            spacing="8"
        ),
        rx.button(
            "Start now",
            color_scheme="purple",
            _hover={"bg": "purple.600"}
        ),
        position="sticky",
        top="0",
        padding_x="2em",
        padding_y="1.5em",
        bg="gray.900",
        box_shadow="0 4px 12px rgba(0, 0, 0, 0.3)",  # sombra para dar profundidad
        z_index="999",
        width="100%"
    )

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "All-in-one Finance App you always wanted", 
                size={"base": "5", "md": "7"},  # más responsive
                text_align="center",
                background_image="linear-gradient(to right, #7C3AED, #EC4899)",
                background_clip="text",
                font_weight="bold"
            ),
            rx.text(
                "Gain control of your finances with our all-in-one finance app. Track your spending, find investment opportunities, and learn.",
                color="gray.300",
                size="4",
                max_width="600px",
                text_align="center"
            ),
            rx.button(
                "Get Started",
                color_scheme="purple",
                size="4",
                _hover={"bg": "purple.600"},
                box_shadow="5"
            ),
            spacing="4",
            align="center"
        ),
        padding_y="6em",
        padding_x="2em",
        bg="gray.900",
        background_image="radial-gradient(circle at top left, #4c1d95 0%, #1a202c 70%)",  # sutil mejora visual
    )
def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.icon(tag=icon, size=32, color="purple.400"),  # Icono más grande y llamativo
            rx.heading(title, size="4", text_align="center"),
            rx.text(description, color="gray.400", size="3", text_align="center"),
            spacing="3",
            align="center"
        ),
        width="100%",
        min_height="200px",
        padding="1.5em",
        variant="ghost",
        border_radius="7",
        box_shadow="md",
        background="radial-gradient(157.73% 157.73% at 50% -29.9%, rgba(203, 213, 225, 0.1) 0%, rgba(203, 213, 225, 0) 100%)",
        border="1px solid #2D3748",
        transition="all 0.3s ease-in-out",
        _hover={"transform": "scale(1.03)", "border_color": "purple.500"}
    )


def features() -> rx.Component:
    features_data = [
        ("lightning-bolt", "Automated Expense Tracking", "Detailed analysis with monthly reports"),
        ("star", "Investment Opportunities", "Best mutual funds and FDs"),
        ("newspaper", "Latest Financial News", "Real-time market updates"),
        ("calculator", "Tax Calculator", "Advanced tax-saving schemes"),
        ("book", "Eclipse Education", "Learn financial literacy"),
        ("pen-tool", "Eclipse for Writers", "Showcase your finance expertise")
    ]
    
    return rx.box(
        rx.vstack(
            rx.heading(
                "Start growing your wealth with Eclipse", 
                size={"base": "5", "md": "6"},
                text_align="center"
            ),
            rx.text(
                "All-in-one personal finance app",
                color="gray.400",
                size="3",
                text_align="center"
            ),
            rx.grid(
                *[feature_card(icon, title, desc) for icon, title, desc in features_data],
                columns="3",
                spacing="5",
                width="100%",
                padding_y="2em"
            ),
            align="center",
            spacing="4",
            padding_y="4em",
            padding_x="2em"
        ),
        bg="gray.900",
        id="features"
    )


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.icon(tag=icon, size=32, color="purple.400"),  # Icono más grande y llamativo
            rx.heading(title, size="4", text_align="center"),
            rx.text(description, color="gray.400", size="3", text_align="center"),
            spacing="3",
            align="center"
        ),
        width="100%",
        min_height="200px",
        padding="1.5em",
        variant="ghost",
        border_radius="xl",
        box_shadow="md",
        background="radial-gradient(157.73% 157.73% at 50% -29.9%, rgba(203, 213, 225, 0.1) 0%, rgba(203, 213, 225, 0) 100%)",
        border="1px solid #2D3748",
        transition="all 0.3s ease-in-out",
        _hover={"transform": "scale(1.03)", "border_color": "purple.500"}
    )


def features() -> rx.Component:
    features_data = [
        ("lightning-bolt", "Automated Expense Tracking", "Detailed analysis with monthly reports"),
        ("star", "Investment Opportunities", "Best mutual funds and FDs"),
        ("newspaper", "Latest Financial News", "Real-time market updates"),
        ("calculator", "Tax Calculator", "Advanced tax-saving schemes"),
        ("book", "Eclipse Education", "Learn financial literacy"),
        ("pen-tool", "Eclipse for Writers", "Showcase your finance expertise")
    ]
    
    return rx.box(
        rx.vstack(
            rx.heading(
                "Start growing your wealth with Eclipse", 
                size={"base": "5", "md": "6"},
                text_align="center"
            ),
            rx.text(
                "All-in-one personal finance app",
                color="gray.400",
                size="3",
                text_align="center"
            ),
            rx.grid(
                *[feature_card(icon, title, desc) for icon, title, desc in features_data],
                columns="3",
                spacing="5",
                width="100%",
                padding_y="2em"
            ),
            align="center",
            spacing="4",
            padding_y="4em",
            padding_x="2em"
        ),
        bg="gray.900",
        id="features"
    )



def pricing_card(plan: str, price: str, features: list, highlighted: bool = False) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.text(plan, color="purple.500", font_weight="medium"),
            rx.heading(price, size="7"),
            rx.divider(),
            rx.vstack(
                *[rx.hstack(
                    rx.icon(tag="check", color="green.500"),
                    rx.text(feature)
                  ) for feature in features],
                spacing="3"
            ),
            rx.button(
                "Get Started" if highlighted else "Learn More",
                color_scheme="purple" if highlighted else "gray",
                width="100%"
            ),
            spacing="4",
            height="100%"
        ),
        border_color="purple.500" if highlighted else "gray.700",
        width="100%"
    )

def pricing() -> rx.Component:
    plans = [
        ("Basic", "$0/mo", ["Expense Tracking", "Basic Reports"], False),
        ("Pro", "$12/mo", ["Advanced Tracking", "Investment Tools"], True),
        ("Enterprise", "$32/mo", ["All Features", "Priority Support"], False)
    ]
    
    return rx.box(
        rx.vstack(
            rx.heading("Simple, transparent pricing", size="6"),
            rx.grid(
                *[pricing_card(plan, price, features, highlight) 
                  for plan, price, features, highlight in plans],
                columns="3",
                spacing="4",
                width="100%",
                padding_y="2em"
            ),
            align="center",
            spacing="4",
            padding_y="4em"
        ),
        bg="gray.900",
        id="pricing"
    )


def footer() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("© 2023 Eclipse Finance"),
            rx.spacer(),
            rx.hstack(
                rx.link(rx.icon("github"), href="#"),
                rx.link(rx.icon("twitter"), href="#"),
                rx.link(rx.icon("linkedin"), href="#"),
                spacing="4"
            ),
            width="100%",
            padding="2em"
        ),
        border_top="1px solid #2D3748",
        bg="gray.900"
    )







def faq() -> rx.Component:
    faq_items = [
        ("What is automated expense tracking?", 
         "Automated expense tracking is a feature that allows you to track your expenses automatically with a single click. It helps you keep track of spending and avoid overspending."),
        ("What kind of investment opportunities does Eclipse provide?", 
         "Eclipse provides you with the best investment opportunities in Mutual Funds and FDs."),
        ("What is Eclipse News?", 
         "Eclipse News is a platform where you can get the latest financial news and market trends."),
        ("What is the advance tax calculator?", 
         "It helps you calculate your tax liability in advance, so you avoid overpaying."),
        ("What is Eclipse Education (for users)?", 
         "A platform where you can learn financial literacy and get tips to better manage your finances."),
        ("What is Eclipse Education (for writers)?", 
         "Writers, bloggers, and influencers can publish content to help improve financial literacy.")
    ]

    return rx.box(
        rx.vstack(
            rx.heading("Frequently Asked Questions", size="6", text_align="center", color="white"),
            rx.text("Learn more about how Eclipse works", color="gray.400", text_align="center"),
            rx.grid(
                *[
                    rx.box(
                        rx.text(question, font_weight="bold", size="4", color="white"),
                        rx.text(answer, size="3", color="gray.300"),
                        padding="1em",
                        border_radius="xl",
                        bg="rgba(255,255,255,0.03)",  # Transparente pero con un leve fondo para legibilidad
                        border="1px solid rgba(255,255,255,0.1)"
                    )
                    for question, answer in faq_items
                ],
                columns="3",
                spacing="4",
                width="100%",
                padding_top="2em"
            ),
            spacing="4",
            padding_y="4em",
            padding_x="2em",
            align="center"
        ),
        bg="transparent",
        id="faq"
    )























app = rx.App()
app.add_page(index)