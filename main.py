import html_generator
import sending_emails


def main(sending_email_with_planner: bool):
    if sending_email_with_planner is True:
        return sending_emails.sending_email_with_planner()
    else:
        print(html_generator.creation_of_html_table())


if __name__ == "__main__":
    main(sending_email_with_planner=False)
