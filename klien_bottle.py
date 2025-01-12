from manim import *

class KleinBottle(ThreeDScene):
    def construct(self):
        # Set up the axes
        axes = ThreeDAxes()

        # Define the Klein bottle parametric function
        def klein_bottle(u, v):
            # Parameters u and v in [0, 2*pi]
            r = 2 + np.cos(u / 2) * np.sin(v) - np.sin(u / 2) * np.sin(2 * v)
            x = r * np.cos(u)
            y = r * np.sin(u)
            z = np.sin(u / 2) * np.sin(v) + np.cos(u / 2) * np.sin(2 * v)
            return np.array([x, y, z])

        # Create the Klein bottle surface
        klein_surface = Surface(
            lambda u, v: klein_bottle(u, v),
            u_range=[0, TAU],  # TAU = 2*pi
            v_range=[0, TAU],
            resolution=(50, 50),  # Increase resolution for smoother surface
            fill_opacity=0.8,
            checkerboard_colors=[BLUE, GREEN],
        )

        # Set up camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, klein_surface)

        # Rotate and display the Klein bottle
        self.play(Create(axes), Create(klein_surface))
        self.begin_ambient_camera_rotation(rate=0.1)  # Slow rotation
        self.wait(8)
        self.stop_ambient_camera_rotation()
        self.wait(2)