insert_departments = '''
insert into departments
  (name)
values
  (%s)
'''

insert_wards = (
    'insert into wards '
    '  (dep_id, name) '
    'values '
    '  (%s, %s) '
)

insert_sponsors = '''
insert into sponsors
  (name)
values
  (%s)
'''

insert_donations = '''
insert into donations
  (sponsor_id, dep_id, date, amount)
values
  (%s, %s, %s, %s)
'''

insert_doctors = '''
insert into doctors
  (dep_id, last_name, first_name, patr_name, salary, premium)
values
  (%s, %s, %s, %s, %s, %s)
'''

insert_vacations = '''
insert into vacations
  (doctor_id, start_date, end_date)
values
  (%s, %s, %s)
'''

insert_specializations = '''
insert into specializations
  (name)
values
  (%s)
'''

insert_doctors_specs = '''
insert into doctors_specs
  (doctor_id, spec_id)
values
  (%s, %s)
'''

