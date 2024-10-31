# Why is the Sky Blue? {#why-is-the-sky-blue}

The sky appears blue due to **Rayleigh scattering**, a phenomenon where
small particles in the atmosphere scatter sunlight. Let’s explore this
further.

## The Basics of Light {#the-basics-of-light}

Light from the sun, although appearing white, is made up of a spectrum
of colors, each with different wavelengths. Here’s a simplified
breakdown:

-   **Red**: Longest wavelength, ~700 nm
-   **Blue**: Shorter wavelength, ~450 nm

This difference in wavelength plays a significant role in how colors
scatter in the atmosphere.

### How Rayleigh Scattering Works {#how-rayleigh-scattering-works}

Rayleigh scattering occurs when light waves encounter particles much
smaller than their wavelengths, primarily **oxygen** and **nitrogen**
molecules in the Earth’s atmosphere. Here’s a summary:

> “The amount of scattering is inversely proportional to the fourth
> power of the wavelength.” — Rayleigh’s Law

Because blue light has a shorter wavelength, it is scattered more than
other colors, making the sky appear predominantly blue.

#### A Brief Comparison of Wavelengths {#a-brief-comparison-of-wavelengths}

| Color | Wavelength (nm) | Scattering Intensity |
|-------|-----------------|----------------------|
| Red   | ~700            | Low                  |
| Green | ~550            | Medium               |
| Blue  | ~450            | High                 |

## What About Sunsets? {#what-about-sunsets}

At sunrise and sunset, sunlight passes through a thicker portion of the
Earth’s atmosphere. This extra distance causes more scattering, allowing
longer wavelengths, like reds and oranges, to dominate the sky.

### Experiment: Scattering in Action {#experiment-scattering-in-action}

You can simulate Rayleigh scattering with a simple experiment:

1.  Fill a glass with water and add a small amount of milk.
2.  Shine a flashlight through the side of the glass.
3.  Observe how the light changes color as it passes through.

This effect demonstrates how scattering increases as the path length
through a medium increases.

## Fun Facts {#fun-facts}

-   The sky on **Mars** appears more reddish due to iron-rich dust in
    its atmosphere.
-   Astronauts in space see a **black sky** because there is no
    atmosphere to scatter sunlight.

### Resources and Further Reading {#resources-and-further-reading}

-   [NASA: Why is the sky
    blue?](https://spaceplace.nasa.gov/blue-sky/en/)
-   [Rayleigh Scattering -
    Wikipedia](https://en.wikipedia.org/wiki/Rayleigh_scattering)

### Code Example: Calculating Scattering Intensity {#code-example-calculating-scattering-intensity}

Here’s a simple Python code snippet that uses Rayleigh’s Law to estimate
scattering intensity:

~~~ python
def rayleigh_scattering(wavelength):
    return 1 / wavelength**4

blue_intensity = rayleigh_scattering(450)  # Approx wavelength for blue
red_intensity = rayleigh_scattering(700)   # Approx wavelength for red

print("Blue scattering intensity:", blue_intensity)
print("Red scattering intensity:", red_intensity)
~~~
