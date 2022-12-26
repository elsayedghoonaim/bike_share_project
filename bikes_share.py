import time
import random
import pandas as pd

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv'}
cities = ['Chicago', 'New York', 'Washington']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']


def get_filters():
    """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            city - name of the city to analyze
            "both" to apply day and month filter
            "none" to apply no filters
        """
    print('hello! let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    # inputs
    city = input('Would you like to see data for Chicago, New York, or Washington?\n').title()
    while city not in cities:
        print('invalid input')
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').title()
    date = input(
        'Would you like to filter the data by month, day, or both? if you don\'t want to filter type "none"\n').title()
    # if no filters
    if date == 'None':
        day = 'All'
        month = 'All'
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif date == 'Day':
        day = input('Which day - Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, or Friday ?\n').title()
        month = 'All'
        while day not in days:
            print('invalid input')
            day = input('Which day - Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, or Friday ?\n').title()
    # TO DO: get user input for month (all, january, february, ... , june)
    elif date == 'Month':
        month = input('Which month -  January, February, March, April, May, or June?\n').title()
        day = 'All'
        while month not in months:
            print('invalid input')
            month = input('Which month -  January, February, March, April, May, or June?\n').title()
    # TO DO: get both day and month
    elif date == 'Both':
        month = input('Which month -  January, February, March, April, May, or June?\n').title()
        while month not in months:
            print('invalid input')
            month = input('Which month -  January, February, March, April, May, or June?\n').title()
        day = input('Which day -  Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
        while day not in days:
            print('invalid input')
            day = input('Which day -  Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
        Asks user to specify a city, month, and day to analyze.

        Args:
            city - name of the city to analyze
            month - name of the month to filter by
            day - name of the day of week to filter by
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """
    df = pd.read_csv(CITY_DATA[city])
    start_time = pd.to_datetime(df['Start Time'])
    df_month = start_time.dt.month
    df_day = start_time.dt.day_name()
    if month != 'All':
        month = months.index(month) + 1
        df = df[df_month == month]
    if day != 'All':
        df = df[df_day == day]

    print('-' * 40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    startt = time.time()

    start_time = pd.to_datetime(df['Start Time'])
    month = start_time.dt.month
    day = start_time.dt.day_name()
    hour = start_time.dt.hour
    # TO DO: display the most common month
    print('The most common month is: {}'.format(months[(month.mode()[0]) - 1]))
    # TO DO: display the most common day of week
    print('The most common day is: {}'.format(day.mode()[0]))
    # TO DO: display the most common start hour
    print('The most common hour is: {}\n'.format(hour.mode()[0]))

    print('This took {} seconds.'.format(time.time() - startt))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    startt = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode()[0]))
    # TO DO: display most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode()[0]))
    # TO DO: display most frequent combination of start station and end station trip
    print('The most common trip is: {}\n'.format((df['Start Station'] + ' to ' + df['End Station']).mode()[0]))

    print('This took {} seconds.'.format(time.time() - startt))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    startt = time.time()

    # TO DO: display total travel time
    print('The total travel time is: {} hours, {} minutes, and {} seconds.'.format(df['Trip Duration'].sum() // 3600, (
            df['Trip Duration'].sum() % 3600) // 60, (df['Trip Duration'].sum() % 3600) % 60))
    # TO DO: display mean travel time
    print(
        'The average travel time is: {} hours, {} minutes, and {} seconds.\n'.format(df['Trip Duration'].mean() // 3600,
                                                                                     (df[
                                                                                          'Trip Duration'].mean() % 3600) // 60,
                                                                                     (df[
                                                                                          'Trip Duration'].mean() % 3600) % 60))
    print('This took {} seconds.'.format(time.time() - startt))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    startt = time.time()

    # TO DO: Display counts of user types
    print('The users types is:\n{}'.format(df['User Type'].value_counts()))
    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('Gender is not available for this city')
    else:
        print('The genders are:\n{}'.format(df['Gender'].value_counts()))
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Birth Year is not available for this city')
    else:
        print('The earliest year of birth is: {}'.format(df['Birth Year'].min()))
        print('The latest year of birth is: {}'.format(df['Birth Year'].max()))
        print('The most common year of birth is: {}\n'.format(df['Birth Year'].mode()[0]))

    print('This took {} seconds.'.format(time.time() - startt))
    print('-' * 40)


def display_raw_data(df):
    """Displays 5 random raws from the data frame"""
    startt = time.time()
    answer = input('would you want to see 5 rows of data? Enter yes or no.\n').lower()
    # Check if the user wants to display 5 random raws
    while answer == 'yes':
        num = random.randint(0, len(df.index) - 5)
        print(df[num:num + 5])
        answer = input('More rows? Enter yes or no.\n')

    print('This took {} seconds.'.format(time.time() - startt))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
