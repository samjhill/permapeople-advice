# Permaculture Advice

Analyzes your garden with the goal of improving its performance, with an eye toward permaculture principles.


## Setup

Set up your python virtual environment:

```shell
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

Set up your API key:

```shell
nano .env
```

Paste your OpenAI API key in:

```
OPENAI_API_KEY=....
```

## Running it

Create a garden plan at [Permapeople.org](https://permapeople.org/plans/new) and save it. 

![garden plan example](images/garden.png)


Open up the developer tools, go to the Application tab, and copy the json blob contained in the `value` field into save-data.json (located in the root of this project).

![image of save data location](images/savedata.png)

```shell
python3 -m main
```

## Example Output

To optimize your garden layout using permaculture principles, there are several key areas to focus on: plant spacing, companion planting, sunlight exposure, irrigation efficiency, and accessibility for maintenance. Here's a breakdown of how you can improve your garden's growth and yield:

### Plant Spacing
- **Trees and Shrubs**: Ensure that fruit trees such as apples, peaches, and persimmons are spaced adequately to avoid competition for resources. The current spacing seems reasonable, but for better air circulation and sunlight penetration, ensure at least 15-20 feet between mature trees like apples and peaches.
- **Bushes and Small Plants**: Lavender and blueberries are positioned fairly close to other plants. While this can create beneficial microclimates, ensure that there’s enough space (around 3-4 feet) to account for their mature size and airflow.

### Companion Planting
- **Lavender**: It is a good companion to fruit trees due to its pest-repelling properties. Its presence near the blueberries and fruit trees is beneficial.
- **Elderberry**: It can serve as a windbreak and attract beneficial insects. Ensure it’s well-integrated with other plants for mutual benefits.
- **Fruit Trees**: Consider underplanting with nitrogen-fixing plants or herbs that attract pollinators for enhanced mutual benefits.

### Sunlight Exposure
- Assess sunlight exposure throughout the day, ensuring that sun-loving plants receive adequate light. Fruit trees generally require full sun, so avoid shading each other or critical areas.
- **Shade Considerations**: Larger trees like Japanese Maple should be positioned to avoid casting extensive shade over sun-loving plants like peaches and apples.

### Irrigation Efficiency
- **Drip Irrigation**: Implement a drip irrigation system to ensure water reaches the root systems efficiently while reducing evaporation.
- **Mulching**: Use mulch around your plants to retain soil moisture, suppress weeds, and enrich the soil as it breaks down.

### Accessibility for Maintenance
- Ensure pathways are sufficiently wide (2-3 feet minimum) and clear for easy access to plants for maintenance tasks such as pruning, harvesting, and monitoring plant health.
- Consider the position of structures like the shed for easy access to tools and resources.

### General Adjustments
- **Streamlining Layout**: Place small plants and herbs strategically under or between larger shrubs and trees to maximize space usage and create layered plantings.
- **Wind Breaks**: If the garden faces strong winds, use taller shrubs or hedges as windbreaks on the windward sides.

By optimizing these aspects, you can create a garden that thrives with improved growth and yield. Regularly assess your garden's specific microclimates and soil conditions for tailored adjustments.