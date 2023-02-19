import tkinter as tk


def widget(data):
    weather_main = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    temp_feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    visibility = data["visibility"]
    wind_speed = data["wind"]["speed"]
    cloudiness = data["clouds"]["all"]
    city_name = data["name"]
    country = data["sys"]["country"]
    try:
        rain = data["rain"]["1h"]
    except KeyError:
        rain = 0

    main_widget = tk.Tk()
    main_widget.geometry("445x561")
    main_widget.resizable(False, False)
    main_widget.configure(bg='black')

    walking_colour_est = 10
    driving_colour_est = 10
    running_colour_est = 10
    cycling_colour_est = 10
    ice_skating_colour_est = 10
    swimming_colour_est = 10
    gym_colour_est = 10

    if visibility < 500:
        cycling_colour_est = cycling_colour_est - 3
        driving_colour_est = driving_colour_est - 3
        running_colour_est = running_colour_est - 1
        swimming_colour_est = swimming_colour_est - 1
    if rain > 0.1:
        walking_colour_est = walking_colour_est - 2
        running_colour_est = running_colour_est - 1
        cycling_colour_est = cycling_colour_est - 1
    if rain > 1.5:
        walking_colour_est = walking_colour_est - 2
        driving_colour_est = driving_colour_est - 1
        running_colour_est = running_colour_est - 3
        cycling_colour_est = cycling_colour_est - 3
    if cloudiness > 60:
        walking_colour_est = walking_colour_est - 1
        swimming_colour_est = swimming_colour_est - 1
    if wind_speed > 12.5:
        cycling_colour_est = cycling_colour_est - 1
    if wind_speed > 25:
        cycling_colour_est = cycling_colour_est - 4
        walking_colour_est = walking_colour_est - 1
        running_colour_est = running_colour_est - 2
        ice_skating_colour_est = ice_skating_colour_est - 2
    if temp_max > 0:
        ice_skating_colour_est = ice_skating_colour_est - 10
    if humidity > 80 or humidity < 15:
        walking_colour_est = walking_colour_est - 1
        running_colour_est = running_colour_est - 2
        cycling_colour_est = cycling_colour_est - 2
        ice_skating_colour_est = ice_skating_colour_est - 1
        swimming_colour_est = swimming_colour_est - 2
    if temp_min < -10 or temp_feels_like < -5:
        walking_colour_est = walking_colour_est - 1
        running_colour_est = running_colour_est - 2
        cycling_colour_est = cycling_colour_est - 2
        driving_colour_est = driving_colour_est - 1
        swimming_colour_est = swimming_colour_est - 4
    if temp_min < 9 or temp_feels_like < 12:
        running_colour_est = running_colour_est - 2
        cycling_colour_est = cycling_colour_est - 1
        swimming_colour_est = swimming_colour_est - 2
    if temp_max > 2.5 or temp > 1:
        ice_skating_colour_est = ice_skating_colour_est - 10
    if pressure > 1024 or pressure < 991:
        walking_colour_est = walking_colour_est - 1
        driving_colour_est = driving_colour_est - 1
        running_colour_est = running_colour_est - 1
        cycling_colour_est = cycling_colour_est - 1
        ice_skating_colour_est = ice_skating_colour_est - 1
        gym_colour_est = gym_colour_est - 2
        swimming_colour_est = swimming_colour_est - 1

    if walking_colour_est < 5:
        walking_colour = "red"
    elif 4 < walking_colour_est < 7:
        walking_colour = "orange"
    else:
        walking_colour = "green"

    if driving_colour_est < 5:
        driving_colour = "red"
    elif 4 < driving_colour_est < 7:
        driving_colour = "orange"
    else:
        driving_colour = "green"

    if running_colour_est < 5:
        running_colour = "red"
    elif 4 < running_colour_est < 7:
        running_colour = "orange"
    else:
        running_colour = "green"

    if ice_skating_colour_est < 4:
        ice_skating_colour = "red"
    elif 3 < ice_skating_colour_est < 6:
        ice_skating_colour = "orange"
    else:
        ice_skating_colour = "green"

    if cycling_colour_est < 4:
        cycling_colour = "red"
    elif 3 < cycling_colour_est < 7:
        cycling_colour = "orange"
    else:
        cycling_colour = "green"

    if swimming_colour_est < 4:
        swimming_colour = "red"
    elif 3 < swimming_colour_est < 6:
        swimming_colour = "orange"
    else:
        swimming_colour = "green"

    if gym_colour_est < 4:
        gym_colour = "red"
    elif 3 < gym_colour_est < 6:
        gym_colour = "orange"
    else:
        gym_colour = "green"

    header_label = tk.Label(main_widget, text=f"Weather in {city_name}, {country}", anchor="center",
                            height=2, width=28, font=("Fixedsys", 20), bg="#737373")
    header_label.grid(column=0, row=0, sticky='nsew')

    overall_data_label = tk.Label(main_widget, height=1, width=25, font=("Fixedsys", 17), bg="#7d7d7d",
                                  text=f"{weather_main.capitalize()}, Fell-like: {round(temp_feels_like)}°C",
                                  anchor="center")
    overall_data_label.grid(column=0, row=1, sticky='nsew')

    data_label = tk.Label(main_widget, height=6, width=25, font=("Fixedsys", 15), bg="#9b9b9b",
                          text=f"Temperature: {round(temp)}°C\nCloudiness: {cloudiness}%\nPressure: "
                               f"{pressure} hPa\nWind: {round(wind_speed * 18 / 5)} km/h \nRain: {rain} mm",
                          anchor="center")
    data_label.grid(column=0, row=2, sticky='nsew')

    activities_label = tk.Label(main_widget, width=25, font=("Fixedsys", 12), bg="#919191",
                                text=f"Activities:", anchor="center")
    activities_label.grid(column=0, row=3, sticky='nsew')

    walking_label = tk.Label(main_widget, height=2, width=25, font=("Fixedsys", 14), bg=walking_colour, text="Walking")
    walking_label.grid(column=0, row=4, sticky='nsew')

    driving_label = tk.Label(main_widget, height=2, width=25, font=("Fixedsys", 14), bg=driving_colour,
                             text="Driving")
    driving_label.grid(column=0, row=5, sticky='nsew')

    running_label = tk.Label(main_widget, height=2, width=25, font=("Fixedsys", 14), bg=running_colour,
                             text="Running")
    running_label.grid(column=0, row=6, sticky='nsew')

    cycling_label = tk.Label(main_widget, height=2, width=25, font=("Fixedsys", 14), bg=cycling_colour,
                             text="Cycling")
    cycling_label.grid(column=0, row=7, sticky='nsew')

    ice_skating_label = tk.Label(main_widget, height=2, width=25, font=("Fixedsys", 14), bg=ice_skating_colour,
                                 text="Ice Skating")
    ice_skating_label.grid(column=0, row=8, sticky='nsew')

    swimming_label = tk.Label(main_widget, height=2, width=25, font=("Fixedsys", 14), bg=swimming_colour,
                              text="Swimming")
    swimming_label.grid(column=0, row=9, sticky='nsew')

    gym_label = tk.Label(main_widget, height=2, width=25, font=("Fixedsys", 14), bg=gym_colour, text="Gym")
    gym_label.grid(column=0, row=10, sticky='nsew')

    main_widget.mainloop()