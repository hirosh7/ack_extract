import service


def main():

    show_the_header()
    episode_data = service.download_data('https://talkpython.fm/episodes/rss')

    latest_show_id, oldest_show_id = service.get_latest_id(episode_data)
    display_results(episode_data, latest_show_id, oldest_show_id)


def display_results(episode_data, latest_show_id, oldest_show_id):
    print(f'Working with total of {latest_show_id} episodes')
    start = oldest_show_id
    end = latest_show_id
    for show_id in range(start, end):
        # Get episode
        info = episode_data.get(show_id)
        print(f'{info.show_id}. {info.title}')


def show_the_header():
    print(f'Welcome to the talk python info downloader')
    print()


if __name__ == '__main__':
    main()
